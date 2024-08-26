from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from patrimonio.models import Item, Contacontabil
from usuario.models import Usuario, Setor
from datetime import datetime, timedelta
from django.utils.timezone import now
from django.http import JsonResponse
from django.db.models import Sum
from collections import Counter
from .forms import ItemSearchForm
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import xlwt


@login_required(login_url='login-page')
def localizacao(request):
    form = ItemSearchForm()
    item = None
    item_searched = False

    if request.method == 'GET' and 'tombo' in request.GET:
        form = ItemSearchForm(request.GET)
        if form.is_valid():
            tombo = form.cleaned_data['tombo']
            item = Item.objects.filter(tombo=tombo).first()
            item_searched = True

    context = {
        'form': form,
        'item': item,
        'item_searched': item_searched,
    }
    return render(request, 'app/localizacao.html', context)


@login_required(login_url='login-page')
def estoque(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(email=request.user.email)
            setor = usuario.setor_id_setor
            # Ordena os itens pela data de compra, do mais recente para o mais antigo
            itens = Item.objects.filter(setor_id_setor=setor).order_by('-datacompra')

            # Configura o paginator para mostrar 10 itens por página
            paginator = Paginator(itens, 10)

            # Pega o número da página atual
            page_number = request.GET.get('page')

            # Pega os itens da página atual
            page_obj = paginator.get_page(page_number)

            context = {
                'page_obj': page_obj,
                'nome_setor': setor.setor_full  # Passa o nome completo do setor para o template
            }

        except Usuario.DoesNotExist:
            return render(request, 'app/erro.html', {'mensagem': 'Usuário não encontrado.'})

        return render(request, 'app/estoque.html', context)
    else:
        return render(request, 'app/estoque.html', {'page_obj': []})

# Dashboard e Views de itens no Dashboard:


@login_required(login_url='login-page')
def dashboardpage(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(email=request.user.email)
            setor = usuario.setor_id_setor
            context = {
                'orgao': setor.orgao_abrev
            }
            return render(request, "app/dashboard.html", context=context)

        except Usuario.DoesNotExist:
            return render(request, "app/dashboard.html")


@login_required(login_url='login-page')
def retorna_quantidade_setores(request):
    quantidade = Setor.objects.count()
    return JsonResponse({'quantidade': quantidade})


@login_required(login_url='login-page')
def retorna_total_gasto(request):
    total = Item.objects.all().aggregate(Sum('valorcompra'))['valorcompra__sum']
    return JsonResponse({'total': total})


@login_required(login_url='login-page')
def relatorio_gasto(request):
    x = Item.objects.all()
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    datacompra = []
    labels = []
    const = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12):
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        y = sum([i.valorcompra for i in x if i.datacompra.month == mes and i.datacompra.year == ano])
        labels.append(meses[mes - 1])
        datacompra.append(y)
        const += 1
    data_json = {'datacompra': datacompra[::-1], 'labels': labels[::-1]}
    return JsonResponse(data_json)


@login_required(login_url='login-page')
def relatorio_marcas(request):
    # Recupera a soma do valor de compra para cada marca em uma única consulta
    marcas_valores = (Item.objects
                      .values('marca')
                      .annotate(total_valorcompra=Sum('valorcompra'))
                      .order_by('-total_valorcompra'))

    # Separa as marcas e os valores somados em listas
    labels = [item['marca'] for item in marcas_valores]
    data = [item['total_valorcompra'] for item in marcas_valores]

    # Cria o JSON com todas as marcas e os valores
    data_jsn = {'labels': labels, 'data': data}

    # Retorna o JSON
    return JsonResponse(data_jsn)


@login_required(login_url='login-page')
def relatorio_setor(request):
    x = Item.objects.all()
    contador_setores = Counter(item.setor_id_setor for item in x)
    soma_valorcompra_por_setor = {}
    for setor, count in contador_setores.items():
        soma_valorcompra_por_setor[setor] = x.filter(setor_id_setor=setor).aggregate(Sum('valorcompra'))[
            'valorcompra__sum']
    labels = [str(setor) for setor in soma_valorcompra_por_setor.keys()]
    data = list(soma_valorcompra_por_setor.values())
    z = list(zip(labels, data))

    z.sort(key=lambda item: item[1], reverse=True)
    z = list(zip(*z))
    return JsonResponse({'labels': z[0], 'data': z[1]})


def relatorio_gasto_por_conta_contabil(request):
    # Definir a data inicial e final do intervalo de 12 meses
    data_final = now()
    data_inicial = data_final - timedelta(days=365)

    # Lista de meses fixos no formato abreviado em português, iniciando em setembro
    meses = ['set', 'out', 'nov', 'dez', 'jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago']

    # Obter os anos envolvidos no intervalo
    ano_atual = data_final.year
    ano_anterior = data_inicial.year

    # Dicionário para armazenar os dados
    dados_mensais = {}
    contas_contabeis = Contacontabil.objects.all()

    # Inicializar dicionário para armazenar os dados
    for conta in contas_contabeis:
        dados_mensais[conta.idcontacontabil] = [0] * 12  # Lista com 12 zeros para 12 meses

    # Agregar dados de gastos por mês e conta contábil
    items = Item.objects.filter(datacompra__range=[data_inicial, data_final]).values(
        'contacontabil_idcontacontabil', 'datacompra__year', 'datacompra__month'
    ).annotate(
        total_gasto=Sum('valorcompra')
    ).order_by('contacontabil_idcontacontabil', 'datacompra__year', 'datacompra__month')

    # Preencher dados agregados
    for item in items:
        conta_id = item['contacontabil_idcontacontabil']
        ano = item['datacompra__year']
        mes = item['datacompra__month']

        # Calcular a posição do mês dentro do intervalo de 12 meses, começando em setembro
        posicao = (mes + 3) % 12  # Mapeia o mês 9 (setembro) para a posição 0 e assim por diante

        total = item['total_gasto']
        dados_mensais[conta_id][posicao] += total

    # Preparar dados para o dataset "Gasto Geral"
    datacompra_geral = [0] * 12
    for i in range(12):
        mes = (data_final.month - i - 1) % 12 + 1
        ano = data_final.year - (1 if mes > data_final.month else 0)
        y = sum([
            i['total_gasto'] for i in items
            if i['datacompra__month'] == mes and i['datacompra__year'] == ano
        ])
        posicao = (mes + 3) % 12  # Mesma lógica de mapeamento para garantir alinhamento
        datacompra_geral[posicao] = y

    # Criar um dicionário para JSON no formato esperado pelo Chart.js
    data = {
        'labels': meses,
        'datasets': [
            {
                'label': str(Contacontabil.objects.get(pk=conta_id)),
                'data': gastos,
            }
            for conta_id, gastos in dados_mensais.items()
        ]
    }

    # Adicionar o dataset "Gasto Geral"
    data['datasets'].append({
        'label': 'GASTOS SEPLAN',
        'data': datacompra_geral,  # Alinhado para começar em setembro
    })

    return JsonResponse(data)


# Fim das views da Dashboard e itens da dashboard


def export_estoque_xls(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(email=request.user.email)
            setor = usuario.setor_id_setor
            itens = Item.objects.filter(setor_id_setor=setor)

            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="estoque.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('Estoque')

            # Cabeçalho da planilha
            row_num = 0
            font_style = xlwt.XFStyle()
            font_style.font.bold = True

            columns = ['Nome', 'Marca', 'Nota Fiscal', 'Data de Compra', 'Preço', 'Tombo']

            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)

            # Corpo da planilha
            font_style = xlwt.XFStyle()

            for item in itens:
                row_num += 1
                ws.write(row_num, 0, item.itemnome, font_style)
                ws.write(row_num, 1, item.marca, font_style)
                ws.write(row_num, 2, item.notafiscal, font_style)
                ws.write(row_num, 3, item.datacompra, font_style)
                ws.write(row_num, 4, item.valorcompra, font_style)
                ws.write(row_num, 5, item.tombo, font_style)

            wb.save(response)
            return response

        except Usuario.DoesNotExist:
            return render(request, 'app/erro.html', {'mensagem': 'Usuário não encontrado.'})

    return HttpResponse("Usuário não autenticado.", status=401)


def export_estoque_pdf(request):
    if request.user.is_authenticated:
        try:
            # Recupera o setor do usuário autenticado
            usuario = Usuario.objects.get(email=request.user.email)
            setor = usuario.setor_id_setor
            itens = Item.objects.filter(setor_id_setor=setor)

            # Configura a resposta HTTP para gerar o PDF
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="estoque.pdf"'

            # Configura o documento PDF
            doc = SimpleDocTemplate(response, pagesize=A4)
            elements = []

            # Estilos de texto
            styles = getSampleStyleSheet()
            title_style = styles['Title']
            normal_style = styles['Normal']

            # Adiciona o título do documento
            elements.append(Paragraph("Relatório de Estoque", title_style))
            elements.append(Paragraph(f"Setor: {setor.setor_abrev}", normal_style))
            elements.append(Paragraph(f"Gerado por: {request.user.username}", normal_style))
            elements.append(Paragraph(" ", normal_style))  # Espaço em branco

            # Adiciona uma tabela com os dados dos itens
            data = [['Nome', 'Marca', 'Nota Fiscal', 'Data da Compra',
                     'Preço', 'Item Tombo']]

            for item in itens:
                data.append([
                    item.itemnome,
                    item.marca,
                    item.notafiscal,
                    item.datacompra,
                    item.valorcompra,
                    item.tombo,

                ])

            # Configura a tabela
            table = Table(data)
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 10),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ]))

            elements.append(table)

            doc.build(elements)

            return response

        except Usuario.DoesNotExist:
            return render(request, 'app/erro.html', {'mensagem': 'Usuário não encontrado.'})

    return HttpResponse("Usuário não autenticado.", status=401)

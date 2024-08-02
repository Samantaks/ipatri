from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patrimonio.models import Item
from usuario.models import Usuario
from datetime import datetime
from django.http import JsonResponse
from django.db.models import Sum
from collections import Counter


@login_required(login_url='login-page')
def estoque(request):
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(idusuario=request.user.id)
        setor = usuario.setor_id_setor
        itens = Item.objects.filter(setor_id_setor=setor)
        context = {
            'itens': itens
        }
        return render(request, 'app/estoque.html', context)
    else:
        return render(request, 'app/estoque.html', {'itens': []})

@login_required(login_url='login-page')
def dashboardpage(request):
    return render(request, "app/dashboard.html")


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
    x = Item.objects.all()
    contador_marcas = Counter(item.marca for item in x)
    soma_valorcompra_por_marca = {}
    for marca, count in contador_marcas.items():
        soma_valorcompra_por_marca[marca] = x.filter(marca=marca).aggregate(Sum('valorcompra'))['valorcompra__sum']
    labels = list(soma_valorcompra_por_marca.keys())
    data = list(soma_valorcompra_por_marca.values())
    z = list(zip(labels, data))
    z.sort(key=lambda item: item[1], reverse=True)
    z = list(zip(*z))
    return JsonResponse({'labels': z[0][:3], 'data': z[1][:3]})


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
    return JsonResponse({'labels': z[0][:2], 'data': z[1][:2]})

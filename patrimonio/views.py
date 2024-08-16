from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ItensCadastroForm, ItemSearchForm, EditItemSetorForm
from .models import Item, Alocacao
from django.core.paginator import Paginator
from django.utils import timezone
from usuario.models import Usuario,Setor


@login_required(login_url='login-page')
def itemcadastro(request):
    form = ItensCadastroForm
    context = {'form': form}
    if request.method == 'GET':
        return render(request, "app/itens_cadastro.html", context=context)

    elif request.method == 'POST':
        form = ItensCadastroForm(request.POST)
        if form.is_valid():
            new_item_nome = form.cleaned_data['ItemNome']
            new_item_tombo = form.cleaned_data['ItemTombo']
            new_item_descricao = form.cleaned_data['ItemDescricao']
            new_item_marca = form.cleaned_data['ItemMarca']
            new_item_preco = form.cleaned_data['ItemPreco']
            new_item_ano = form.cleaned_data['ItemAno']
            new_item_data = form.cleaned_data['ItemData']
            new_item_notafiscal = form.cleaned_data['ItemNotaFiscal']
            new_item_depreciacao = form.cleaned_data['ItemDepreciacao']
            new_item_setor = form.cleaned_data['ItemSetor']

            new_item_salvo = Item(
                descricao=new_item_descricao,
                datacompra=new_item_data,
                tombo=new_item_tombo,
                marca=new_item_marca,
                notafiscal=new_item_notafiscal,
                valorcompra=new_item_preco,
                itemnome=new_item_nome,
                itemano=new_item_ano,
                depreciacao_iddepreciacao1=new_item_depreciacao,
                setor_id_setor=new_item_setor
            )

            new_item_salvo.save()

            return render(request, "app/itens_cadastro.html", context=context)

        return render(request, "app/itens_cadastro.html", context=context)

    return render(request, "app/itens_cadastro.html", context=context)


@login_required(login_url='login-page')
def itemmov(request):
    search_form = ItemSearchForm()
    edit_form = None
    item = None
    item_searched = False

    if request.method == 'GET' and 'tombo' in request.GET:
        search_form = ItemSearchForm(request.GET)
        if search_form.is_valid():
            tombo = search_form.cleaned_data['tombo']
            item = Item.objects.filter(tombo=tombo).first()
            item_searched = True
            if item:
                edit_form = EditItemSetorForm(instance=item)

    if request.method == 'POST' and 'item_id' in request.POST:
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        edit_form = EditItemSetorForm(request.POST, instance=item)
        if edit_form.is_valid():
            # Salva a alteração no setor do item
            edit_form.save()

            # Busca o usuário na tabela Usuario, baseado no usuário logado
            usuario = Usuario.objects.get(email=request.user.email)

            # Captura a data e hora da movimentação informada pelo usuário
            dataalocacao = edit_form.cleaned_data['dataalocacao']

            # Cria uma nova instância de Alocacao para registrar a movimentação
            Alocacao.objects.create(
                item_idpatrimonio=item,
                dataalocacao=dataalocacao,  # Usa a data e hora informada pelo usuário
                user=usuario  # Registrar o usuário que fez a movimentação
            )

            # Reseta os formulários
            edit_form = None
            item = None
            search_form = ItemSearchForm()

    context = {
        'search_form': search_form,
        'edit_form': edit_form,
        'item': item,
        'item_searched': item_searched,
    }
    return render(request, 'app/itens-mov.html', context)


@login_required(login_url='login-page')
def itemvisita(request):
    # Primeira parte da View - Listagem geral dos itens
    itens = Item.objects.filter(datacompra__lte=timezone.now()).order_by('datacompra')
    paginatorgeral = Paginator(itens, 5)
    page_number = request.GET.get('page')
    page_obj = paginatorgeral.get_page(page_number)

    # Segunda parte da View - Busca de item por tombo
    form = ItemSearchForm()
    visita_list = request.session.get('visita_list', [])  # Recupera a lista de tombos da sessão
    searched = False

    if request.method == 'GET' and 'tombo' in request.GET:
        form = ItemSearchForm(request.GET)
        if form.is_valid():
            tombo = form.cleaned_data['tombo']
            item = Item.objects.filter(tombo=tombo).first()
            searched = True

            if item and item.tombo not in visita_list:
                visita_list.append(item.tombo)  # Armazene apenas o tombo na lista
                request.session['visita_list'] = visita_list  # Atualiza a sessão com a nova lista

    # Recupera os objetos Item com base nos tombos armazenados na sessão
    itens_buscados = Item.objects.filter(tombo__in=visita_list)

    context = {
        'page_obj': page_obj,
        'form': form,
        'searched': searched,
        'visita_list': itens_buscados  # Passa os itens buscados para o template
    }

    return render(request, "app/itens-visita.html", context)
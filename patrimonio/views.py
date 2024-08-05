from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from patrimonio.forms import ItensCadastroForm
from .models import Item
from usuario.models import Setor


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

        context = {'form': form}

        return render(request, "app/itens_cadastro.html", context=context)

    return render(request, "app/itens_cadastro.html", context=context)


@login_required(login_url='login-page')
def itemvisita(request):
    return render(request, "app/itens-visita.html")


@login_required(login_url='login-page')
def itemmov(request):
    form = ItensCadastroForm
    context = {'form': form}
    return render(request, "app/itens-mov.html", context=context)

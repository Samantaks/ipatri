from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patrimonio.forms import ItensCadastroForm
from .models import Item


@login_required(login_url='login-page')
def itemcadastro(request):
    form = ItensCadastroForm
    context = {'form': form}
    if request.method == 'GET':
        return render(request, "app/itens_cadastro.html", context=context)

    else:
        new_item_nome = request.POST.get('ItemNome')
        new_item_tombo = request.POST.get('ItemTombo')
        new_item_descricao = request.POST.get('ItemDescricao')
        new_item_marca = request.POST.get('ItemMarca')
        new_item_preco = request.POST.get('ItemPreco')
        new_item_ano = request.POST.get('ItemAno')
        new_item_data = request.POST.get('ItemData')
        new_item_notafiscal = request.POST.get('ItemNotafiscal')

        new_item_salvo = Item( descricao= new_item_descricao, datacompra= new_item_data , tombo=new_item_tombo, marca=new_item_marca, notafiscal=new_item_notafiscal,
                              valorcompra=new_item_preco, itemnome=new_item_nome, itemano=new_item_ano)
        new_item_salvo.save()

    return render(request, "app/itens_cadastro.html", context=context)


@login_required(login_url='login-page')
def itemvisita(request):
    form = ItensCadastroForm
    context = {'form': form}
    return render(request, "app/itens-visita.html", context=context)


@login_required(login_url='login-page')
def itemmov(request):
    form = ItensCadastroForm
    context = {'form': form}
    return render(request, "app/itens-mov.html", context=context)

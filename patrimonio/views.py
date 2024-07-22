from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from patrimonio.forms import ItensCadastroForm
from .models import Item


@login_required(login_url='login-page')
def itemcadastro(request):
    if request.method == 'GET':
        form = ItensCadastroForm
        context = {'form': form}
        return render(request, "app/itens_cadastro.html", context=context)

    else:
        form = ItensCadastroForm(request.POST, request.FILES)
        context = {'form': form}
        if form.is_valid():
            new_item_nome = form.cleaned_data['ItemNome']
            new_item_tombo = form.cleaned_data['ItemTombo']
            new_item_marca = form.cleaned_data['ItemMarca']
            new_item_cc = form.cleaned_data['ItemContaContabil']
            new_item_preco = form.cleaned_data['ItemPreco']
            new_item_ano = form.cleaned_data['ItemAno']
            new_item_notafiscal = form.cleaned_data['ItemNotaFiscal']

            new_item_salvo = Item(tombo=new_item_tombo, marca=new_item_marca,
                                  conta_contabil=new_item_cc, notafiscal=new_item_notafiscal,
                                  valorcompra=new_item_preco, itemnome=new_item_nome, itemano=new_item_ano)

            new_item_salvo.save()
            return redirect('itemcadastro')

        return render(request, "app/itens_cadastro.html", context=context)

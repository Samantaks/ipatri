from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login-page')
def itemcadastro(request):
    return render(request, "app/itens_cadastro.html")

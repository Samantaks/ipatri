from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login-page')
def dashboardpage(request):
    return render(request, "app/dashboard.html")


@login_required(login_url='login-page')
def estoquepage(request):
    return render(request, "app/estoque.html")


@login_required(login_url='login-page')
def localizacaopage(request):
    return render(request, "app/estoque.html")


@login_required(login_url='login-page')
def manutencaopage(request):
    return render(request, "app/manutencao.html")

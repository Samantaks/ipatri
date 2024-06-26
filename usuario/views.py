from django.shortcuts import render


# Create your views here.
def loginpage(request):
    return render(request, "usuario/login-page.html")


def cadastropage(request):
    return render(request, "usuario/cadastro-page.html")

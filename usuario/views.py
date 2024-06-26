from django.shortcuts import render


# Create your views here.
def loginpage(request):
    return render(request, "login-page.html")


def cadastropage(request):
    return render(request, "cadastro-page.html")

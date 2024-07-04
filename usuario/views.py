from usuario.forms import LoginForm
from django.shortcuts import render


# Create your views here.
def loginpage(request):
    if request.method == "GET":
        form = LoginForm
        context = {
            'form': form,
        }
        return render(request, 'usuario/login-page.html', context=context)
    else:
        form = LoginForm(request.POST)
        print(form.is_valid())
        form = LoginForm(request.POST)
        context = {
            'form': form,
        }
        return render(request, 'usuario/login-page.html', context=context)


def cadastropage(request):
    return render(request, "usuario/cadastro-page.html")

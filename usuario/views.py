from usuario.forms import LoginForm, CadastroForm
from django.shortcuts import render


def loginpage(request):
    if request.method == "GET":
        form = LoginForm
        context = {
            'form': form,
        }
        return render(request, 'usuario/login-page.html', context=context)
    else:
        form = LoginForm(request.POST)
        context = {
            'form': form,
        }

        return render(request, "usuario/login-page.html", context=context)


def cadastropage(request):
    if request.method == "GET":
        form = CadastroForm
        context = {
            'form': form,
        }
        return render(request, 'usuario/cadastro-page.html', context=context)
    else:
        form = CadastroForm(request.POST)
        context = {
            'form': form,
        }


        return render(request, 'usuario/cadastro-page.html', context=context)

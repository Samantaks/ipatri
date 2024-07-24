from usuario.forms import LoginForm, CadastroForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Usuario
from django.http.response import HttpResponse


def loginpage(request):
    form = LoginForm
    context = {
        'form': form,
    }
    if request.method == "GET":
        return render(request, "usuario/login-page.html", context=context)

    else:
        username = request.POST.get('cpf')
        password = request.POST.get('senha')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse("Usuário autenticado com sucesso")
        else:
            return HttpResponse("Usuário com dedos errados.")


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

        nome = request.POST.get('fname')
        sobrenome = request.POST.get('lname')
        email = request.POST.get('Email')
        username = request.POST.get('cpf')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse("Já existe um usuário com esse CPF")

        user = User.objects.create_user(username=username, email=email,
                                        password=senha, first_name=nome, last_name=sobrenome)
        user.save()

        new_nome = request.POST.get('fname')
        new_sobrenome = request.POST.get('lname')
        new_email = request.POST.get('Email')
        new_senha = request.POST.get('senha')
        new_cpf = request.POST.get('cpf')

        new_usuario = Usuario(nomeusuario=new_nome, sobrenome=new_sobrenome,
                              email=new_email, senha=new_senha, cpf=new_cpf)
        new_usuario.save()
    return render(request, 'usuario/cadastro-page.html', context=context)

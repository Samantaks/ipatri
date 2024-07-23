from usuario.forms import LoginForm, CadastroForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib import auth
from django.http import HttpResponseNotFound


def loginpage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        context = {
            'form': form,
        }
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        try:
            usuario = Usuario.objects.get(cpf=cpf)
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
            return render(request, 'usuario/login-page.html', {'form': form})

            # Verifique a senha
        if usuario.senha == senha:
            # Se a senha estiver correta, faça o login do usuário
            login(request, usuario)
            return render(request, 'app/dashboard.html')  # Redirecione para a página inicial ou outra página desejada
        else:
            messages.error(request, 'Senha incorreta.')
    else:
        form = LoginForm()

    return render(request, 'usuario/login-page.html', {'form': form})


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

        if form.is_valid():
            new_nome = form.cleaned_data['fname']
            new_sobrenome = form.cleaned_data['lname']
            new_email = form.cleaned_data['Email']
            new_senha = form.cleaned_data['senha']
            new_cpf = form.cleaned_data['cpf']

            new_Usuario = Usuario(nomeusuario=new_nome, sobrenome=new_sobrenome, email=new_email, senha=new_senha,
                                  role=1, cpf=new_cpf)
            new_Usuario.save()

            return redirect('cadastro-page')

        return render(request, 'usuario/cadastro-page.html', context=context)

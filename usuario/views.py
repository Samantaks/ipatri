from usuario.forms import LoginForm, CadastroForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from django.contrib.auth.models import User


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
        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

# Form Renderizado em cima

        validUserDjango = User.objects.filter(username=cpf).first()
        validSenhaDjango = User.objects.filter(password=senha)
        validSenhaDB = Usuario.objects.filter(senha=senha)
        validUserDB = Usuario.objects.filter(cpf=cpf).first()

        if validUserDjango:
            if validSenhaDjango:
                return HttpResponse(f'Bem vindo {cpf}')
            else:
                return HttpResponse('Usuário com a senha errada no loop do Django.')

        elif validUserDB:
            if validSenhaDB:
                return HttpResponse(f'Bem vindo {cpf}')
            else:
                return HttpResponse(f'Usuário com senha errada no loop do DB')
        else:
            return HttpResponse("Usuário inválido.")


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

            return redirect('usuario:cadastro')

        return render(request, 'usuario/cadastro-page.html', context=context)

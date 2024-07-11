from usuario.forms import LoginForm, CadastroForm
from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login


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

        validSenhaDB = Usuario.objects.filter(senha=senha)
        validUserDB = Usuario.objects.filter(cpf=cpf).first()
        validarDjango = authenticate(username=cpf, password=senha)

        if validarDjango:
            login(request, validarDjango)
            return redirect('app-home')

        elif validUserDB:
            if validSenhaDB:
                return redirect('app-home')
            else:
                return render(request, 'usuario/login-page.html', context=context)

        else:
            return render(request, 'usuario/login-page.html', context=context)


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

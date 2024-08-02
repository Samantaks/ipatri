from usuario.forms import LoginForm, CadastroForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Usuario


@login_required
def perfil(request):
    try:
        usuario = Usuario.objects.get(cpf=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important, to keep the user logged in after password change
            return redirect('perfil')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {
        'usuario': usuario,
        'form': form
    }

    return render(request, 'app/usuario_page.html', context)


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
            return render(request, 'app/dashboard.html', context=context)
        else:
            return HttpResponse("Usuário com dedos errados.")


def cadastropage(request):
    form = CadastroForm
    context = {
        'form': form,
    }
    if request.method == "GET":
        return render(request, 'usuario/cadastro-page.html', context=context)
    else:
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


@login_required(login_url='login-page')
def bio(request):
    return render(request, 'app/usuario_page.html')

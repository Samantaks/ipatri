from usuario.forms import LoginForm, CadastroForm, UsuarioSearchForm, EditUsuarioSetorForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Usuario
from django.contrib import messages
from django.contrib.messages import constants
from rolepermissions.roles import assign_role


# Mudar o setor de um usuário
@login_required(login_url='login-page')
def usuario_setor(request):
    search_form = UsuarioSearchForm()
    edit_form = None
    usuario = None
    usuario_searched = False

    if request.method == 'GET' and 'cpf' in request.GET:
        search_form = UsuarioSearchForm(request.GET)
        if search_form.is_valid():
            cpf = search_form.cleaned_data['cpf']
            usuario = Usuario.objects.filter(cpf=cpf).first()
            usuario_searched = True
            if usuario:
                edit_form = EditUsuarioSetorForm(instance=usuario)

    if request.method == 'POST' and 'usuario_id' in request.POST:
        usuario_id = request.POST.get('usuario_id')
        usuario = get_object_or_404(Usuario, pk=usuario_id)
        edit_form = EditUsuarioSetorForm(request.POST, instance=usuario)
        if edit_form.is_valid():
            edit_form.save()
            edit_form = None
            usuario = None
            search_form = UsuarioSearchForm()

    context = {
        'search_form': search_form,
        'edit_form': edit_form,
        'usuario': usuario,
        'usuario_searched': usuario_searched,
    }
    return render(request, 'app/setor_servidor.html', context)


# Página de Perfil de usuário
@login_required(login_url='login-page')
def perfil(request):
    try:
        usuario = Usuario.objects.get(email=request.user.email)
    except Usuario.DoesNotExist:
        usuario = None

    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('perfil')
    else:
        form = PasswordChangeForm(user=request.user)

        context = {
            'usuario': usuario,
            'form': form
            }
        return render(request, 'app/usuario_page.html', context)


# Logar usuário:
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
            return redirect('/app/')
        else:
            messages.add_message(request, constants.ERROR, "Já existe um usuário com o CPF")
            return redirect('/login/')


# Cadastrar usuário:
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
        conf_email = request.POST.get('ConfEmail')
        username = request.POST.get('cpf')
        senha = request.POST.get('senha')
        conf_senha = request.POST.get('ConfSenha')

        user = User.objects.filter(username=username).first()
        if user:
            messages.add_message(request, constants.ERROR, "Já existe um usuário com o CPF")
            return redirect('/cadastro/')

        if not senha == conf_senha:
            messages.add_message(request, constants.ERROR, "A senha colocada é diferente da confirmada")
            return redirect('/cadastro/')

        if not email == conf_email:
            messages.add_message(request, constants.ERROR, "O email colocado é diferente do confirmado")
            return redirect('/cadastro/')

        user = User.objects.create_user(username=username, email=email,
                                        password=senha, first_name=nome, last_name=sobrenome)
        user.save()
        assign_role(user,'servidor')

        new_nome = request.POST.get('fname')
        new_sobrenome = request.POST.get('lname')
        new_email = request.POST.get('Email')
        new_senha = request.POST.get('senha')
        new_cpf = request.POST.get('cpf')

        new_usuario = Usuario(nomeusuario=new_nome, sobrenome=new_sobrenome,
                              email=new_email, senha=new_senha, cpf=new_cpf)

        new_usuario.save()
        return redirect('/login/')

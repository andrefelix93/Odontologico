from acesso.forms import CadastroForms, LoginForms
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():

            nome=form['nome_cadastro'].value()
            usuario_login=form['usuario_login'].value()
            email=form['email'].value()
            senha=form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                    messages.error(request, "Usuário já existente")
                    return redirect('acesso:login')

            usuario = User.objects.create_user(
                first_name=nome,
                username=usuario_login,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('acesso:login')


    return  render(request, "pages/register.html", {"form": form})

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome=form['usuario_login'].value()
            senha=form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f" Usuário {nome} logado com sucesso!")
                return redirect('home')
            else:
                messages.error(request, "Erro ao efetuar login")
                return redirect('login')

    return render(request, "pages/login.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Usúario deslogado")
    return redirect('login')

def home(request):
    
    return render(request, "pages/index.html")
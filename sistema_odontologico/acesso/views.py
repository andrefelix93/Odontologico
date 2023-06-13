from django.shortcuts import render, redirect

from usuarios.forms import LoginForms,CadastroForms

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():

            nome=form['nome_cadastro'].value()
            email=form['email'].value()
            senha=form['senha1'].value()

            if User.objects.filter(username=nome).exists():
                    messages.error(request, "Usuário já existente")
                    return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('login')


    return  render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Usúario deslogado")
    return redirect('login')
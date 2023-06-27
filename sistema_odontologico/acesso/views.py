from acesso.forms import CadastroForms, LoginForms
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from paciente.forms import CadastroPacienteForms
from paciente.models import Paciente


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
            nome=form['nome_login'].value()
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
                return redirect('acesso:login')

    return render(request, "pages/login.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Usúario deslogado")
    return redirect('acesso:login')

def home(request):
    if not request.user.is_authenticated:
        return redirect('acesso:login')
    
    return render(request, "pages/index.html")

def cadastro_paciente(request):
    form = CadastroPacienteForms()

    if request.method == 'POST':
        form = CadastroPacienteForms(request.POST)

        if form.is_valid():

            nome=form['nome_paciente'].value()
            email=form['email'].value()
            sexo=form['sexo'].value()
            data_nascimento=form['data_nascimento_paciente'].value()
            cpf=form['cpf_paciente'].value()
            telefone_celular=form['telefone_celular_paciente'].value()

            if Paciente.objects.filter(cpf_paciente=cpf).exists():
                    return HttpResponse('Já cadastrado!')
                   
            
            paciente = Paciente.objects.create(
                    nome_paciente=nome,
                    sexo=sexo,
                    cpf_paciente=cpf,
                    email=email,
                    data_nascimento_paciente=data_nascimento,
                    telefone_celular_paciente=telefone_celular,
                )
            paciente.save()
            messages.success(request, "Paciente cadastrado com sucesso!")
            return redirect('home')


    return  render(request, "pages/register_pacient.html", {"form": form})
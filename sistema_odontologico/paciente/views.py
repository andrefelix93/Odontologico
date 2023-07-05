from django.http import HttpResponse
from django.shortcuts import redirect, render
from paciente.forms import CadastroPacienteForms
from paciente.models import Paciente


# Create your views here.
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
            #messages.success(request, "Paciente cadastrado com sucesso!")
            return redirect('home')
        else:
            return HttpResponse(' ERRO!')


    return  render(request, "pages/register_pacient.html", {"form": form})
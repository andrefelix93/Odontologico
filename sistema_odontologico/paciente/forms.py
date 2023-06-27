from django import forms
from paciente.models import Paciente


class CadastroPacienteForms(forms.ModelForm):
        data_nascimento_pacientewidget=forms.DateInput(format='%d/%m/%Y')
        class Meta:
                # Modelo base
                model = Paciente

                # Campos que estarão no form
                fields = (
                        'nome_paciente',
                        'email',
                        'sexo',
                        'data_nascimento_paciente',
                        'cpf_paciente',
                        'telefone_celular_paciente',
                )
        

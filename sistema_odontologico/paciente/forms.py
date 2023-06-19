from django import forms
from paciente.models import Paciente


class CadastroPacienteForms(forms.Form):
        nome_paciente = forms.CharField(
                label = "Nome",
                required = True,
                max_length = 100,
                widget = forms.TextInput(
                    attrs = {
                        "class": "form-control form-label",
                        
                    }
                )
        )

        email_paciente = forms.EmailField(
                label = "Email",
                required = True,
                max_length = 100,
                widget = forms.EmailInput(
                    attrs = {
                        "class": "form-control form-label",
                        
                    }
                )
        )

        SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        )

        sexo = forms.ChoiceField(
                label = "Sexo",
                choices = SEXO_CHOICES,
                required = True,
        )

        data_nascimento_paciente = forms.DateField(
                label = "Data de Nascimento",
                required = True,
        )

        cpf_paciente = forms.CharField(
                label = "CPF",
                max_length=14, 
                required = True, 
                widget = forms.TextInput(
                    attrs = {
                        "class": "form-control form-label",
                    }
                )
        )
        
        telefone_celular_paciente = forms.CharField(
                label = "Celular do Paciente",
                max_length=15, 
                required = True, 
                widget = forms.TextInput(
                    attrs = {
                        "class": "form-control form-label",
                    }
                )
        )

        class Meta:
                # Modelo base
                model = Paciente

                # Campos que estarão no form
                fields = [
                        'nome_paciente',
                        'email_paciente',
                        'sexo',
                        'data_nascimento_paciente',
                        'cpf_paciente',
                        'telefone_celular_paciente',
                ]
        

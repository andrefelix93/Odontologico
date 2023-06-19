from django import forms


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

        sexo = forms.CharField(
                label = "Sexo",
                choices = SEXO_CHOICES,
                max_length = 1,
                blank = False,
                null = False,
        )

        data_nascimento_paciente = forms.DateField(
                label = "Data de Nascimento",
                placeholder = "Data de Nascimento",
                required = True,
                max_length = 100,
        )

        cpf_paciente = forms.CharField(
                label = "CPF",
                placeholder = "CPF",
                max_length=14, 
                blank=False, 
                null=False
        )
        
        telefone_celular_paciente = forms.CharField(
                label = "Celular do Paciente",
                placeholder = "Celular do Paciente",
                max_length=15, 
                blank=False, 
                null=False
        )

        

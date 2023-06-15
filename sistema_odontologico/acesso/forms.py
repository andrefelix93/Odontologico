import unidecode
from django import forms
from django.contrib.auth.models import User


class CadastroForms(forms.Form):

    nome_cadastro=forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-label",
                
            }
        )
    )
    usuario_login=forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-label",
                
            }
        )
    )
    email=forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-label",
                
            }
        )
    )
    senha1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-label",
                
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirme sua Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-label",
                
            }
        )
    )
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Espaços não são permitidos nesse campo")
            if unidecode.unidecode(nome) != nome:
                raise forms.ValidationError("O nome de cadastro não pode conter acentuação.")
            else:
                return nome
    def clean_senha_2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha1 and senha_2:
            if senha1 != senha_2:
                raise forms.ValidationError("As senhas digitadas são diferentes e precisam ser iguais")
            else:
                return senha_2
            
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name')        
            
class LoginForms(forms.Form):

    nome_login=forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite Sua Senha"
            }
        )
    )
import datetime

from django.db import models
from django.forms import ValidationError


def validate_date(value):
    try:
        # Verifica se o valor da data pode ser convertido corretamente
        datetime.datetime.strptime(value, '%d/%m/%Y')
    except ValueError:
        # Caso a conversão falhe, levanta uma exceção de validação
        raise ValidationError('Formato de data inválido (dd/mm/aaaa)')
    
# Create your models here.
class Paciente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )

    nome_paciente = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    data_nascimento_paciente = models.CharField(
        verbose_name='Data de Nascimento',
        max_length=10,
        validators=[validate_date],
    )
    email = models.EmailField(null=False, blank=False)
    cpf_paciente = models.CharField(max_length=14, blank=False, null=False)
    telefone_celular_paciente = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self) -> str:
        return self.nome_paciente
    

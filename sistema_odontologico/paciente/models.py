from django.db import models


# Create your models here.
class Paciente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )

    nome_paciente = models.CharField(max_length=100, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    data_nascimento_paciente = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    cpf_paciente = models.CharField(max_length=14, blank=False, null=False)
    telefone_celular_paciente = models.CharField(max_length=15, blank=False, null=False)

    def __str__(self) -> str:
        return self.nome_paciente
    

from django.urls import path
from paciente import views

app_name = 'paciente'

urlpatterns = [
    path('cadastro-paciente/', views.cadastro_paciente, name="cadastro-paciente"),
    path('buscar-paciente/', views.buscar_paciente, name="buscar-paciente"),
]
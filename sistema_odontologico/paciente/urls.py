from acesso import views
from django.urls import path

app_name = 'paciente'

urlpatterns = [
    path('cadastro-paciente/', views.cadastro_paciente, name="cadastro-paciente"),
]
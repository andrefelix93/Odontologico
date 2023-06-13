from django.urls import path
from acesso import views

app_name = 'acesso'

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
    path('', views.home, name="home"),
]
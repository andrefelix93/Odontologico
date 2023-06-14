from acesso import views
from django.urls import path

app_name = 'acesso'

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
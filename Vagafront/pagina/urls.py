from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio),
    path('Cadastro/',views.cadastro, name = "cadastro"),
    path('Usuarios/',views.usuarios, name = 'usuarios'),
    path('inicio/',views.inicio, name = 'inicio'),
]
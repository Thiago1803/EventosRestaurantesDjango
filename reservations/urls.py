from django.urls import path
from . import views

urlpatterns = [
    path('ver_vagas/', views.ver_vagas, name='ver_vagas'),
    path('abrir_vagas/', views.abrir_vagas, name='abrir_vagas'),
]

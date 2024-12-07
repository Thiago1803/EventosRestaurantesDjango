from django.urls import path
from . import views

urlpatterns = [
    path('ver_minhas_reservas/', views.ver_minhas_reservas, name='ver_minhas_reservas'),
    path('ver_vagas/<int:restaurante_id>/', views.ver_vagas, name='ver_vagas'),
    path('reservar/<int:restaurante_id>/', views.reservar_vaga, name='reservar_vaga'),
    path('abrir_vagas/', views.abrir_vagas, name='abrir_vagas'),
]

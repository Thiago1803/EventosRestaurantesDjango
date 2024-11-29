from django.db import models
from django.core.validators import MinValueValidator
from restaurants.models import Restaurants
from django.contrib.auth.models import User 

class Reservations(models.Model):
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE, related_name='restaurants', verbose_name='Reservas')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customers', verbose_name='Cliente')

    number_reservations = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name='Quantidade de Reservas')

    date_reservation = models.DateTimeField(verbose_name="Data da Reserva") # indica a data da reserva
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Marcado em") # indica quando o usuario clicou para reservar a vaga

    def __str__(self):
        return f'Reservas em {self.restaurante.name}'
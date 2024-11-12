from django.contrib import admin
from .models import Restaurants


@admin.register(Restaurants) # aqui faz aparecer o menuzinho de restaurantes la no ambiete admin
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    list_display_links = ('name',)
    search_fields = ('name',)
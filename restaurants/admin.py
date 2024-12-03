from django.contrib import admin
from .models import Restaurants, Food, Category


@admin.register(Restaurants) # aqui faz aparecer o menuzinho de restaurantes la no ambiete admin
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'phone', 'display_foods', 'display_categories', 'image',)
    list_display_links = ('name',)
    search_fields = ('name', 'city',)
    filter_horizontal = ('menu', 'category', )

    # Função para exibir as comidas associadas ao restaurante
    def display_foods(self, obj):
        return ", ".join([food.name for food in obj.menu.all()]) 
    display_foods.short_description = 'Menu'

    # Função para exibir as categorias associadas ao restaurante
    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.category.all()])
    display_categories.short_description = 'Categorias'



@admin.register(Food) # aqui faz aparecer o menuzinho de comidas la no ambiete admin
class FoodsAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Category) # aqui faz aparecer o menuzinho de categorias la no ambiete admin
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
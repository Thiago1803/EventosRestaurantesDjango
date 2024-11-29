from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as django_logout
from restaurants.models import Restaurants


def logout_view(request):
    django_logout(request)  # Desloga o usuário de fato
    return render(request, 'login.html')  # Redireciona para a página de login


def home(request):
    city = request.GET.get('city', None)  # Pegando a cidade que foi buscada, se nada foi buscado entao o valor é "none"
    food = request.GET.get('food', None)  # Pegando a comida que foi buscada, se nada foi buscado entao o valor é "none"
    restaurant = request.GET.get('restaurant_name', None)  # Pegando o restaurante que foi buscado, se nada foi buscado entao o valor é "none"
    category = request.GET.get('category', None)  # Pegando a categoria selecionada, se nada foi selecionado entao o valor é "none"
    
    restaurantes = Restaurants.objects.all() # Pega todos os restaurantes salvos
    if restaurant: restaurantes = restaurantes.filter(name__icontains=restaurant) # Mantenho apenas os que são da cidade buscada em 'city'
    if city: restaurantes = restaurantes.filter(city__icontains=city) # Mantenho apenas os que são da cidade buscada em 'city'
    if food: restaurantes = restaurantes.filter(menu__name__icontains=food) # Mantenho apenas os que tem a comida buscada em 'food'
    if category: restaurantes = restaurantes.filter(category__name__icontains=category) # Mantenho apenas os que tem a comida buscada em 'food'

    filtros = [
        {'param': 'pub', 'icon': 'local_bar', 'text': 'Pub'},
        {'param': 'lenha', 'icon': 'local_fire_department', 'text': 'Fogão a lenha'},
        {'param': 'local', 'icon': 'public', 'text': 'Cultura local'},
        {'param': 'piscina', 'icon': 'pool', 'text': 'Com piscina'},
        {'param': 'praia', 'icon': 'beach_access', 'text': 'Perto da praia'},
        {'param': 'gastronomia', 'icon': 'restaurant', 'text': 'Gastronomia de autor'},
        {'param': 'romântico', 'icon': 'favorite', 'text': 'Ambiente romântico'},
        {'param': 'vegetariana', 'icon': 'eco', 'text': 'Opções vegetarianas'},
        {'param': 'família', 'icon': 'family_restroom', 'text': 'Para toda a família'},
        {'param': 'música', 'icon': 'music_note', 'text': 'Música ao vivo'},
        {'param': 'espetáculo', 'icon': 'theater_comedy', 'text': 'Espetáculo'}
    ]


    # flg_teve_busca é para indicar se o usuário buscou algo, só para controlar a mensagem exibida na tela inicial
    return render(request, 'index.html', {'restaurantes': restaurantes, 'flg_teve_busca': bool(city or food or restaurant or category), 'filtros': filtros})

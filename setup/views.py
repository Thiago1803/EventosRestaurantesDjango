from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as django_logout
from restaurants.models import Restaurants


def logout_view(request):
    django_logout(request)  # Desloga o usuário de fato
    return render(request, 'login.html')  # Redireciona para a página de login


def home(request):
    search = request.GET.get('search', None)  # Pegando o que foi buscado e armazenando em "search", se nada foi buscado entao o valor é "none"

    if search:  # Procuro no BD restaurantes que POSSUEM EM SEU NOME o que foi buscado
        restaurantes = Restaurants.objects.filter(name__icontains=search) 
    else:  # Se nada foi buscado, pego tudo
        restaurantes = Restaurants.objects.all()

    filtros = [
        {'param': 'pub', 'icon': 'local_bar', 'text': 'Pub'},
        {'param': 'fogao_a_lenha', 'icon': 'local_fire_department', 'text': 'Fogão a lenha'},
        {'param': 'cultura_local', 'icon': 'public', 'text': 'Cultura local'},
        {'param': 'piscina', 'icon': 'pool', 'text': 'Com piscina'},
        {'param': 'praia', 'icon': 'beach_access', 'text': 'Perto da praia'},
        {'param': 'gastronomia', 'icon': 'restaurant', 'text': 'Gastronomia de autor'},
        {'param': 'romantico', 'icon': 'favorite', 'text': 'Ambiente romântico'},
        {'param': 'vegetariano', 'icon': 'leaf', 'text': 'Opções vegetarianas'},
        {'param': 'familia', 'icon': 'family_restroom', 'text': 'Para toda a família'},
        {'param': 'musica_ao_vivo', 'icon': 'music_note', 'text': 'Música ao vivo'},
        {'param': 'espetaculo', 'icon': 'theater_comedy', 'text': 'Espetáculo'}
    ]

    return render(request, 'index.html', {'restaurantes': restaurantes, 'search': search, 'filtros': filtros})

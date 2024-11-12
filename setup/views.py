from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as django_logout
from restaurants.models import Restaurants


def logout_view(request):
    django_logout(request)  # Desloga o usuário de fato
    return render(request, 'login.html')  # Redireciona para a página de login


def home(request):
    search = request.GET.get('search', None)  # Pegando o que foi buscado e armazenando em "search", se nada foi buscado entao o valor é "none"

    if search: # Procuro no BD restaurantes que POSSUEM EM SEU NOME o que foi buscado
        restaurantes = Restaurants.objects.filter(name__icontains=search) 
    else: # Se nada foi buscado, pego tudo
        restaurantes = Restaurants.objects.all()

    return render(request, 'home.html', {'restaurantes': restaurantes, 'search': search})
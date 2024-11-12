from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout as django_logout


def logout_view(request):
    django_logout(request)  # Desloga o usuário de fato
    return render(request, 'login.html')  # Redireciona para a página de login


def home(request):
    return render(request, 'home.html')
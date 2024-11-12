from django.shortcuts import render
from django.http import HttpResponse
from .models import RestaurantReservations

def ver_vagas(request):
    return render(request, 'ver_vagas.html', {'Restaurante': "esquina"})


def abrir_vagas(request):
    if(request.method == "GET"):
        return render(request, 'abrir_vagas.html', {'Restaurante': "esquina"})
    elif(request.method == "POST"):
        name = request.POST.get('name')
        number_vacancies = request.POST.get('number_vacancies')
        return HttpResponse('Submissao de form')
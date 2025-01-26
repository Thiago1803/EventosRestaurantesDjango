from django.shortcuts import render, redirect
from django.http import HttpResponse
from restaurants.models import Restaurants
from reservations.models import Reservations
from django.db.models import Sum
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse


def ver_vagas(request, restaurante_id):
    try:
        # Pegando o restaurante que o usuário deseja ver as vagas
        restaurante = Restaurants.objects.get(id=restaurante_id)

        # Pegando a data do formulário, se fornecida, ou usando a data atual como padrão
        date_reservation = request.GET.get('date_reservation', datetime.now().date().strftime('%Y-%m-%d'))
        date_reservation = datetime.strptime(date_reservation, '%Y-%m-%d').date()

        # número de vagas do restaurante
        total_vagas = restaurante.total_resevations

        # aqui faz a conta da quantidade de pessoas que maracaram reserva nesse restaurante no dia
        reservas_no_dia = Reservations.objects.filter(
            restaurant=restaurante,
            date_reservation=date_reservation
        ).aggregate(Sum('number_reservations'))['number_reservations__sum'] or 0

        # aqui pega o que falta de vagas
        vagas_disponiveis = total_vagas - reservas_no_dia

        #pega os dados do usuario logado
        client = request.user

        #pega a data atual, para ser o dia minímo permitido para reserva
        today = datetime.now().date().strftime('%Y-%m-%d')


        # Se for uma requisição AJAX, retornar os dados em JSON
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'vagas_disponiveis': vagas_disponiveis,
                'reservation_date': date_reservation.strftime('%Y-%m-%d')
            })
        
        
        #senao é a renderizacao da pagina normal
        return render(request, 'ver_vagas.html', 
            {
                'today': today,'cliente': client,
                'restaurante': restaurante, 'total_vagas': total_vagas, 
                'total_reservas': reservas_no_dia, 'vagas_disponiveis': vagas_disponiveis
            }
        )

    except Restaurants.DoesNotExist:
        return render(request, 'sem_restaurante.html', {'mensagem': 'Restaurante não encontrado!'}) # se o restaurante com o id buscado não existir





def reservar_vaga(request, restaurante_id):
    # pega o restaurante buscado (que é passado pelo GET)
    try: restaurante = Restaurants.objects.get(id=restaurante_id)
    except Restaurants.DoesNotExist: return render(request, 'sem_restaurante.html', {'mensagem': 'Restaurante não encontrado!'})


    # ve se o usuário nao está logado
    if not request.user.is_authenticated:
        return render(request, 'login.html')  # Redireciona para a página de login


    #pega os dados do usuário logado
    client = request.user


    # Pega os dados do formulário e valida eles
    number_reservations = int(request.POST.get('number_reservations'))
    date_reservation = request.POST.get('date_reservation')
    
    if not number_reservations or number_reservations < 1: return messages.error(request, "Número de reservas inválido.")
    
    # Converte a data para o formato DateTime
    try: date_reservation = timezone.datetime.strptime(date_reservation, '%Y-%m-%d')
    except ValueError: return messages.error(request, "Data Inválida.")
    


    # Se passou de tudo acima, cria a reserva
    reserva = Reservations.objects.create(
        restaurant=restaurante,
        client=client,
        number_reservations=number_reservations,
        date_reservation=date_reservation
    )

    #redirect retorna para uma rota, enquanto render apenas renderiza o html
    return redirect('/')
    


def ver_minhas_reservas(request):
    # ve se o usuário nao está logado
    if not request.user.is_authenticated:
        return render(request, 'login.html')  # Redireciona para a página de login
    
    
    client = request.user #pega os dados do usuario logado
    today = datetime.now().date() # data de hoje


    # Filtra as reservas feitas por este usuário
    reservations = (
        Reservations.objects.filter(client=client)
        .values('date_reservation', 'restaurant__id', 'restaurant__name', 'restaurant__image')  # Agrupa por data e restaurante
        .annotate(total_reservations=Sum('number_reservations'))
    )

    # Divide as reservas entre passadas e ativas
    reservas_ativas = [r for r in reservations if r['date_reservation'].date() >= today]
    reservas_passadas = [r for r in reservations if r['date_reservation'].date() < today]

    return render(request, 'minhas_reservas.html', {
        'reservas_ativas': reservas_ativas,
        'reservas_passadas': reservas_passadas,
        'MEDIA_URL': settings.MEDIA_URL
    })


def abrir_vagas(request):
    if(request.method == "GET"):
        return render(request, 'abrir_vagas.html', {'Restaurante': "esquina"})
    elif(request.method == "POST"):
        name = request.POST.get('name')
        number_vacancies = request.POST.get('number_vacancies')
        return HttpResponse('Submissao de form')
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def cadastro(request):
    if(request.method == "GET"):
        return render(request, 'cadastro.html')
    elif(request.method == "POST"):
        # dados do formulario
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')


        # verifica se já existe um usuário no banco de dados com o mesmo login, para nao deixar
        user = User.objects.filter(username=username)
        if(user):
            return HttpResponse("Já existe um usuário com esse login")
        

        # campos para criar usuario
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        return render(request, 'login.html')
        



def login(request):
    if(request.method == "GET"):
        return render(request, 'login.html')
    elif(request.method == "POST"):
        # dados do formulario
        username = request.POST.get('username')
        password = request.POST.get('password')


        # verifica se o login e senha batem com de algum usuário no BD
        user = authenticate(username=username, password=password)
        if(user):
            login_django(request, user) # esse código que de fato irá autenticar o usuário
            return render(request, 'home.html')
        else:
            return HttpResponse("Login ou senha inválidos")
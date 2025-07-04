from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def inicio(request):
    return render(request, 'AppWeb/inicio.html')

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'AppWeb/login.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmar = request.POST['confirmar']

        if password != confirmar:
            messages.error(request, "Las contraseñas no coinciden.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Ese nombre de usuario ya está en uso.")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('inicio')
    return render(request, 'AppWeb/sign_up.html')
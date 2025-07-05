from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm, EditarPerfilForm, CustomPasswordChangeForm, VideojuegoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .models import Videojuego

# Create your views here.

def inicio(request):
    return render(request, 'AppWeb/inicio.html')

def about(request):
    return render(request, "AppWeb/about.html")

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
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'AppWeb/sign_up.html', {'form': form})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        if 'perfil_submit' in request.POST:
            perfil_form = EditarPerfilForm(request.POST, instance=request.user)
            password_form = CustomPasswordChangeForm(user=request.user)
            if perfil_form.is_valid():
                perfil_form.save()
                messages.success(request, 'Perfil actualizado correctamente.')
                return redirect('editar_perfil')
        elif 'password_submit' in request.POST:
            perfil_form = EditarPerfilForm(instance=request.user)
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)
                messages.success(request, 'Contraseña actualizada correctamente.')
                return redirect('editar_perfil')
    else:
        perfil_form = EditarPerfilForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'AppWeb/editar_perfil.html', {
        'perfil_form': perfil_form,
        'password_form': password_form,
    })

def lista_videojuegos(request):
    juegos = Videojuego.objects.all()
    return render(request, 'AppWeb/lista_videojuegos.html', {'juegos': juegos})

@login_required
def crear_videojuego(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'AppWeb/form_videojuego.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_videojuego(request, pk):
    juego = get_object_or_404(Videojuego, pk=pk)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm(instance=juego)
    return render(request, 'AppWeb/form_videojuego.html', {'form': form, 'accion': 'Editar'})

@login_required
def borrar_videojuego(request, pk):
    juego = get_object_or_404(Videojuego, pk=pk)
    if request.method == 'POST':
        juego.delete()
        return redirect('lista_videojuegos')
    return render(request, 'AppWeb/confirma_borrado.html', {'objeto': juego})


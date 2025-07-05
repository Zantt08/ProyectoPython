from django.contrib import admin
from django.urls import path
from AppWeb import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('about/', views.about, name='about'),
    path('perfil/',views.editar_perfil, name='editar_perfil'),
    path('videojuegos/', views.lista_videojuegos, name='lista_videojuegos'),
    path('videojuegos/crear/', views.crear_videojuego, name='crear_videojuego'),
    path('videojuegos/editar/<int:pk>/', views.editar_videojuego, name='editar_videojuego'),
    path('videojuegos/borrar/<int:pk>/', views.borrar_videojuego, name='borrar_videojuego'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
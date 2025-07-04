from django.contrib import admin
from django.urls import path
from AppWeb import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('about/', views.about, name='about'),
    path('perfil/',views.editar_perfil, name='editar_perfil'),
]

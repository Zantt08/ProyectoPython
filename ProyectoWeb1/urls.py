from django.contrib import admin
from django.urls import path
from AppWeb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('login/', views.login_usuario, name='login'),
]

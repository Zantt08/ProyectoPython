from django.db import models

# Create your models here.

class Videojuego(models.Model):
    name = models.CharField("Nombre", max_length=100)
    year = models.PositiveIntegerField("Año de lanzamiento")
    genre = models.CharField("Género", max_length=100)
    developers = models.CharField("Desarrolladores", max_length=100)
    game_image = models.ImageField("Imagen del videojuego", upload_to='game_images/', null=True, blank=True)

    def __str__(self):
        return self.name

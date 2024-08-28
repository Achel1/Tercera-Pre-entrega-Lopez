from django.db import models


# Create your models here.


class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    nivel = models.IntegerField()


class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Descripción no proporcionada")


class Plataforma(models.Model):
    nombre = models.CharField(
        max_length=100
    )  # Nombre de la plataforma (e.g., PC, PlayStation, Xbox)
    fabricante = models.CharField(max_length=100)  # Fabricante de la plataforma


class Juego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)  # Ejemplo: Aventura, Acción

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

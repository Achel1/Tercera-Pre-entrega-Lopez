from django.contrib import admin
from Gamezone.models import Jugador, Juego, Plataforma, Personaje

# Register your models here.

admin.site.register(Juego)
admin.site.register(Jugador)
admin.site.register(Plataforma)
admin.site.register(Personaje)

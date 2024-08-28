from django.urls import path
from Gamezone import views


urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("buscar_info/", views.buscar_info, name="buscar_info"),
    path("resultado/", views.resultado, name="resultado"),
    path("juego/", views.juego, name="juego"),
    path("jugador/", views.jugador, name="jugador"),
    path("plataforma/", views.plataforma, name="plataforma"),
    path("personaje/", views.personaje, name="personaje"),
    path("padre/", views.padre, name="padre"),
    path("", views.inicio, name="inicio"),
    path("buscar/", views.buscar_info, name="buscar_info"),
]

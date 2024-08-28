from django.http import HttpResponse
from datetime import datetime
from datetime import date

from django.template import Template, Context
from Gamezone.models import Jugador, Juego, Plataforma, Personaje


# Saluda
def saludo(request):
    return HttpResponse("Hola Django - Coder")


# otra vista con titulo y parrafo
def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")


# Es para que nos diga el dia de hoy
def dia_de_hoy(request):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")


def muestra_nombre(self, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")


# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context


def probando_template(request):

    nom = "MANUEL"
    ap = "LOPEZ"

    listaDeNotas = [10, 1, 5, 3, 9]

    diccionario = {
        "nombre": nom,
        "apellido": ap,
        "hoy": datetime.now(),
        "notas": listaDeNotas,
    }

    # Abrimos el archivo html
    mi_html = open("./Proyecto1/plantillas/template1.html")

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context(diccionario)

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)


def agregar_curso(request, nom, cam):
    curso = Curso(nombre=nom, camada=cam)
    curso.save()
    return HttpResponse("Curso Agregado")

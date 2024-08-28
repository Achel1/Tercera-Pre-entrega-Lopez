from django.shortcuts import render
from Gamezone.models import Juego, Jugador, Personaje, Plataforma


def juego(request):
    if request.method == "POST":
        titulo = request.POST.get("Titulo")
        genero = request.POST.get("Genero")

        if titulo and genero:
            nuevo_juego = Juego(
                titulo=titulo,
                genero=genero,
            )
            nuevo_juego.save()
            return render(request, "games/inicio.html")
        else:
            # Manejo de error si faltan campos
            return render(
                request, "games/juego.html", {"error": "Faltan campos obligatorios"}
            )

    return render(request, "games/juego.html")


def jugador(request):
    if request.method == "POST":
        nombre = request.POST.get("Nombre")
        nivel = request.POST.get("Nivel")

        if nombre and nivel:
            nuevo_jugador = Jugador(
                nombre=nombre,
                nivel=nivel,
            )
            nuevo_jugador.save()
            return render(request, "games/inicio.html")
        else:
            return render(
                request, "games/jugador.html", {"error": "Faltan campos obligatorios"}
            )

    return render(request, "games/jugador.html")


def personaje(request):
    if request.method == "POST":
        nombre = request.POST.get("Nombre")
        descripcion = request.POST.get("Descripcion")

        if nombre and descripcion:
            nuevo_personaje = Personaje(
                nombre=nombre,
                descripcion=descripcion,
            )
            nuevo_personaje.save()
            return render(request, "games/inicio.html")
        else:
            # Manejo de error si faltan campos
            return render(
                request, "games/personaje.html", {"error": "Faltan campos obligatorios"}
            )

    return render(request, "games/personaje.html")


def padre(request):
    return render(request, "games/padre.html")


def plataforma(request):
    if request.method == "POST":
        nombre = request.POST.get("Nombre")
        fabricante = request.POST.get("Fabricante")

        if nombre and fabricante:
            nueva_plataforma = Plataforma(
                nombre=nombre,
                fabricante=fabricante,
            )
            nueva_plataforma.save()
            return render(request, "games/inicio.html")
        else:
            return render(
                request,
                "games/plataforma.html",
                {"error": "Faltan campos obligatorios"},
            )

    return render(request, "games/plataforma.html")


def inicio(request):
    if request.GET.get("Informacion"):
        nombre = request.GET.get("nombre")
        fabricante = request.GET.get("fabricante")
        plataforma = request.GET.get("plataforma")
        titulo = request.GET.get("titulo")
        genero = request.GET.get("genero")
        nivel = request.GET.get("nivel")
        descripcion = request.GET.get("descripcion")

        # Filtrar en varios modelos
        plataformas = Plataforma.objects.filter(
            nombre__icontains=plataforma,
            fabricante__icontains=fabricante,
        )
        juegos = Juego.objects.filter(
            titulo__icontains=titulo,
            genero__icontains=genero,
        )
        jugadores = Jugador.objects.filter(
            nombre__icontains=nombre,
            nivel__icontains=nivel,
        )
        personajes = Personaje.objects.filter(
            nombre__icontains=nombre,
            descripcion__icontains=descripcion,
        )

        # Pasar todos los resultados al template
        return render(
            request,
            "games/inicio.html",
            {
                "plataformas": plataformas,
                "juegos": juegos,
                "jugadores": jugadores,
                "personajes": personajes,
            },
        )

    return render(request, "games/inicio.html")


def resultado(request):
    # Obtener parámetros de búsqueda del request
    titulo = request.GET.get("titulo", "")
    nombre = request.GET.get("nombre", "")
    fabricante = request.GET.get("fabricante", "")
    plataforma = request.GET.get("plataforma", "")
    genero = request.GET.get("genero", "")
    nivel = request.GET.get("nivel", "")
    descripcion = request.GET.get("descripcion", "")

    # Realizar consultas en la base de datos
    plataformas = Plataforma.objects.filter(
        nombre__icontains=nombre, fabricante__icontains=fabricante
    )

    juegos = Juego.objects.filter(titulo__icontains=titulo, genero__icontains=genero)

    jugadores = Jugador.objects.filter(nombre__icontains=nombre, nivel__icontains=nivel)

    personajes = Personaje.objects.filter(
        nombre__icontains=nombre, descripcion__icontains=descripcion
    )

    # Pasar los resultados a la plantilla
    return render(
        request,
        "games/resultado.html",
        {
            "plataformas": plataformas,
            "juegos": juegos,
            "jugadores": jugadores,
            "personajes": personajes,
        },
    )


def buscar_info(request):
    if request.method == "GET":
        titulo = request.GET.get("titulo", "")
        # Agrega otros campos según sea necesario
        # Aquí puedes agregar más parámetros si el formulario tiene más campos

        plataformas = Plataforma.objects.filter(nombre__icontains=titulo)
        juegos = Juego.objects.filter(titulo__icontains=titulo)
        jugadores = Jugador.objects.filter(nombre__icontains=titulo)
        personajes = Personaje.objects.filter(nombre__icontains=titulo)

        return render(
            request,
            "games/resultado.html",
            {
                "plataformas": plataformas,
                "juegos": juegos,
                "jugadores": jugadores,
                "personajes": personajes,
            },
        )

    return render(request, "games/inicio.html")

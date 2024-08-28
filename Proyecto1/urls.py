"""
URL configuration for Proyecto1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include

# from Proyecto1.views import (
#     saludo,
#     otra_vista,
#     dia_de_hoy,
#     muestra_nombre,
#     probando_template,
#     agregar_curso,
# )
# from . import views
# from django.contrib import admin


# urlpatterns = [
#     path("plantilla/", views.probando_template, name="plantilla"),
# ]
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("saludo/", saludo),
#     path("otra_vista/", otra_vista),
#     path("dia/", dia_de_hoy),
#     path("nombre/<nombre>", muestra_nombre),
#     path("plantillas/", probando_template),
#     path("agregar_curso/<nom>/<cam>", agregar_curso),
#     path("admin/", admin.site.urls),
#     path("Gamezone/", include("Gamezone.urls")),
# ]

from django.contrib import admin
from django.urls import path, include

from Proyecto1.views import (
    saludo,
    otra_vista,
    dia_de_hoy,
    muestra_nombre,
    probando_template,
    agregar_curso,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("saludo/", saludo, name="saludo"),
    path("otra_vista/", otra_vista, name="otra_vista"),
    path("dia/", dia_de_hoy, name="dia_de_hoy"),
    path("nombre/<nombre>/", muestra_nombre, name="muestra_nombre"),
    path("plantillas/", probando_template, name="plantillas"),
    path("agregar_curso/<nom>/<cam>/", agregar_curso, name="agregar_curso"),
    path("Gamezone/", include("Gamezone.urls")),
    path("games/", include("Gamezone.urls")),  # Incluye las rutas de la app Gamezone
]

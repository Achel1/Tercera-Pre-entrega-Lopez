from django import forms


class buscar_info(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    nivel = forms.IntegerField()
    nombre = forms.CharField(max_length=100)
    descripcion = forms.TextField(default="Descripción no proporcionada")
    nombre = forms.CharField(
        max_length=100
    )  # Nombre de la plataforma (e.g., PC, PlayStation, Xbox)
    fabricante = forms.CharField(max_length=100)  # Fabricante de la plataforma
    titulo = forms.CharField(max_length=100)
    genero = forms.CharField(max_length=50)  # Ejemplo: Aventura, Acción

# Generated by Django 5.1 on 2024-08-28 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gamezone', '0003_jugador_personaje_plataforma'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaje',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='plataforma',
            name='fecha_lanzamiento',
        ),
    ]

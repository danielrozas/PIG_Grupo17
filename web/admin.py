from django.contrib import admin

from .models import Clientes, Directores, Generos, Peliculas, Alquiler

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Directores)
admin.site.register(Generos)
admin.site.register(Peliculas)
admin.site.register(Alquiler)
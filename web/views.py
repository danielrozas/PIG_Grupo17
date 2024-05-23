from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.

def index(request):

    # Agrego el diccionario context con dos variables de contexto
    context ={
        'nombre': 'Carlos',
        'fecha_hora': datetime.datetime.now()
    }

    return render(request, 'web/index.html', context)

def saludar(request, nombre):
    return HttpResponse(f"<h1>Bienvenido {nombre}</h1>")

def alumnos_por_año(request, year):
    alumnos = ["Carlos", "Maria", "Jose"]
    return HttpResponse(f"Listado de Alumnos: {year} \n {alumnos}")

def listado_alumnos(request):
    contexto={}
    return render(request, 'web/listado_alumnos.html', contexto)
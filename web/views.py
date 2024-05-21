from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def saludar(request, nombre):
    return HttpResponse(f"<h1>Bienvenido {nombre}</h1>")

def alumnos_por_año(request, year):
    alumnos = ["Carlos", "Maria", "Jose"]
    return HttpResponse(f"Listado de Alumnos: {year} \n {alumnos}")
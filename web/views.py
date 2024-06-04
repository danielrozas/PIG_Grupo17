from django.shortcuts import render
from django.views.generic import ListView
from .models import Peliculas

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def listar_peliculas(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'web/peliculas.html', {'peliculas': peliculas})
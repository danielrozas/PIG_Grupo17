from django.shortcuts import render, redirect
from .models import Peliculas
from .forms import PeliculaForm

# Create your views here.
def index(request):
    return render(request, 'web/index.html')

def listar_peliculas(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'web/peliculas.html', {'peliculas': peliculas})
    
def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_peliculas')
    else:
        form = PeliculaForm()
    
    return render(request, 'web/agregar_pelicula.html', {'form': form})
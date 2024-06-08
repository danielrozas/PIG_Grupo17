from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib import messages
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
    

def eliminar_pelicula(request, pelicula_id):
    try:
        pelicula = Peliculas.objects.get(id=pelicula_id)
    except Peliculas.DoesNotExist:
        raise Http404("La película que intentas eliminar no existe.")
    if request.method == 'POST':
        pelicula.delete()
        messages.success(request, 'La película se eliminó exitosamente.')
        return redirect('lista_peliculas')
    return render(request, 'web/eliminar_pelicula.html', {'pelicula': pelicula})
    
def lista_peliculas_admin(request):
    peliculas = Peliculas.objects.all()
    return render(request, 'web/lista_peliculas.html', {'peliculas': peliculas})
    
def index_admin(request):
    return render(request, 'web/index_admin.html')
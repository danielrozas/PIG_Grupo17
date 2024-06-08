from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.contrib import messages
from .models import Peliculas, Directores, Generos
from .forms import PeliculaForm, DirectorForm, GeneroForm
from django.views.generic.list import ListView

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
            messages.success(request, 'La película se agregó con éxito')
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

class PeliculasListView(ListView):
    model=Peliculas
    context_object_name='peliculas'
    template_name='web/lista_peliculas.html'
    ordering = ['AnioLanzamiento']
    
def index_admin(request):
    return render(request, 'web/index_admin.html')
    
def agregar_director(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El director se agregó con éxito')
            return redirect('lista_directores')
    else:
        form = DirectorForm()
    
    return render(request, 'web/agregar_director.html', {'form': form})

def agregar_genero(request):
    if request.method == "POST":
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El género se agregó con éxito')
            return redirect('lista_generos')
    else:
        form = GeneroForm()
    
    return render(request, 'web/agregar_genero.html', {'form': form})
    
def lista_directores(request):
    directores = Directores.objects.all()
    return render(request, 'web/lista_directores.html', {'directores': directores})

def lista_generos(request):
    generos = Generos.objects.all()
    return render(request, 'web/lista_generos.html', {'generos': generos})

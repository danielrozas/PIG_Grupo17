from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from django.contrib import messages
from .models import Peliculas, Directores, Generos, Clientes, Alquiler
from .forms import PeliculaForm, DirectorForm, GeneroForm, SignupForm, AlquilerForm
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib.auth import logout, login

# Create your views here.
def index(request):
    peliculas_recientes = Peliculas.objects.filter()[:10]
    return render(request, 'web/index.html', {'peliculas_recientes': peliculas_recientes})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            direccion = form.cleaned_data.get('direccion')
            Clientes.objects.create(user=user, Direccion=direccion)
            login(request, user)
            messages.success(request, 'Se registró con éxito')
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'web/registration/signup.html', {'form': form})

def user_logout(request):
    logout(request)

    messages.success(request, 'Sesion Cerrada')

    return redirect('index')

def listar_peliculas(request):
    actualizar_estados()
    peliculas = Peliculas.objects.all()
    return render(request, 'web/peliculas.html', {'peliculas': peliculas})

@login_required   
def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'La película se agregó con éxito')
            return redirect('listar_peliculas')
        else:
            print("Errores en el formulario:", form.errors)
    else:
        form = PeliculaForm()
    
    return render(request, 'web/agregar_pelicula.html', {'form': form})

@login_required
def modificar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Peliculas, id=pelicula_id)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            messages.success(request, 'La película se modificó con éxito')
            return redirect('listar_peliculas')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'web/modificar_pelicula.html', {'form': form, 'pelicula': pelicula})

@login_required
def eliminar_pelicula(request, pelicula_id):
    try:
        pelicula = Peliculas.objects.get(id=pelicula_id)
    except Peliculas.DoesNotExist:
        raise Http404("La película que intentas eliminar no existe.")
    if request.method == 'POST':
        pelicula.delete()
        messages.success(request, 'La película se eliminó exitosamente.')
        return redirect('listar_peliculas')
    return render(request, 'web/eliminar_pelicula.html', {'pelicula': pelicula})

@login_required
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

@login_required
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
    
class DirectoresListView(LoginRequiredMixin, ListView):
    model = Directores
    context_object_name = 'directores'
    template_name = 'web/lista_directores.html'
class GenerosListView(LoginRequiredMixin, ListView):
    model = Generos
    context_object_name = 'generos'
    template_name = 'web/lista_generos.html'

@login_required
def lista_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, 'web/lista_clientes.html', {'clientes': clientes})

@login_required(login_url='/web/accounts/login/')
def alquilar_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Peliculas, id=pelicula_id)
    cliente = get_object_or_404(Clientes, user=request.user)
    
    if request.method == 'POST':
        form = AlquilerForm(request.POST)
        if form.is_valid() and pelicula.Disponibilidad:
            alquiler = form.save(commit=False)
            alquiler.Cliente_id = cliente
            alquiler.Pelicula_id = pelicula
            alquiler.FechaInicio = timezone.now().date()
            alquiler.Estado = True
            alquiler.PrecioTotal = (alquiler.FechaFin - alquiler.FechaInicio).days * pelicula.PrecioAlquiler
            alquiler.save()
            messages.success(request, 'Su película se alquiló con éxito')
            pelicula.CantidadDisponible -= 1
            if pelicula.CantidadDisponible == 0:
                pelicula.Disponibilidad = False
            pelicula.save()
            return redirect('lista_peliculas_alquiladas')
    else:
        form = AlquilerForm()
    
    return render(request, 'web/alquilar_pelicula.html', {'form': form, 'pelicula': pelicula})

def actualizar_estados():
    alquileres_activos = Alquiler.objects.filter(Estado=True)
    for alquiler in alquileres_activos:
        if alquiler.FechaFin < timezone.now().date():
            alquiler.Estado = False
            alquiler.Pelicula_id.Disponibilidad = True
            alquiler.Pelicula_id.save()
            alquiler.save()

@login_required
def lista_peliculas_alquiladas(request):
    alquileres = Alquiler.objects.filter(Cliente_id=request.user.clientes)
    return render(request, 'web/lista_peliculas_alquiladas.html', {'alquileres': alquileres})

@login_required
def listar_alquileres(request):
    alquileres = Alquiler.objects.all().select_related('Cliente_id', 'Pelicula_id')
    return render(request, 'web/lista_alquileres.html', {'alquileres': alquileres})
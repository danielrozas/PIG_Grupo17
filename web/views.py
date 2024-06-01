from django.shortcuts import render

import datetime

from .models import Clientes, Directores, Generos, Peliculas

from django.views.generic import (DetailView)

# Create your views here.

def index(request):

    context ={
        'nombre_sistema': 'Sistema Alquiler Películas',
        'nombre_empresa': 'Blockbuster',
        'fecha_hora': datetime.datetime.now()
    }

    return render(request, 'web/index.html', context)


# ----------------------------------------------
# Clientes
# ----------------------------------------------
# 
class ClienteDetailView(DetailView):
     model = Clientes
     template_name = "web/cliente_detail.html"
     context_object_name = 'cliente'

     def get_object(self, queryset=None):
        return Clientes.objects.get(pk=1)
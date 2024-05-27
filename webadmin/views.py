from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,
                                  ListView, 
                                  TemplateView
                                  )


import datetime

# Create your views here.

from .models import *

# def index(request):
#     return render(request, 'webadmin/index.html')

class InicioView(TemplateView):
    """Vista que carga la página de inicio"""
    template_name= 'webadmin/index.html'

# ====================================
# Actores
# ====================================
# Agregar Actor
# ====================================
class ActorCreateView(CreateView):
    model = Actores
    template_name = "webadmin/Actores/add_actor.html"

    fields = [
        'NombreActor'
    ]
 
    success_url = reverse_lazy('web_app:correcto')

    def form_valid(self, form):
        # Logica del Proceso
        actor = form.save(commit=False)
        actor.save()
        return super(ActorCreateView, self).form_valid(form)

# ====================================
# Mostrar Actor
# ====================================
class ActorDetailView(DetailView):
    model = Actores
    template_name = "webadmin/Actores/read_actor.html"

    def get_context_data(self, **kwargs):
        context = super(ActorDetailView, self).get_context_data(**kwargs)
        #
        # Aca pongo un proceso para recuperar el actor
        #
        context['titulo'] = 'Empleado del Mes'
        return context
    

# ====================================
# Actualizar Actor
# ====================================
class ActorUpdateView(UpdateView):
        model = Actores
        template_name = "webadmin/Actores/update_actor.html"
        fields = [
        'NombreActor'
        ]

        success_url = reverse_lazy('persona_app:correcto')

        def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            print('****** METODO post ******')
            print('=========================')
            print(request.POST)
            print(request.POST['NombreActor'])
            return super().post(request, *args, **kwargs)

        def form_valid(self, form):
            # Logica del Proceso
            print('****** METODO form_valid ******')         
            return super(ActorUpdateView, self).form_valid(form)  

   

# ====================================
# Borrar Actor
# ====================================
class ActorDeleteView(DeleteView):
        model = Actores
        template_name = "webadmin/Actores/delete_actor.html"
        success_url = reverse_lazy('persona_app:correcto')




class SuccessView(TemplateView):
        template_name = "actor/success.html"


# ====================================    
# 
class OpcionesTablaView(TemplateView):
    template_name = 'webadmin/opciones_tabla.html'

    # Para pasar variables 
    def get_context_data(self, **kwargs):
        context = super(OpcionesTablaView, self).get_context_data(**kwargs)
        # If don´t call 'super', you wont have the context processor variables
        # like 'user'
        context['Nombre_de_Archivo'] = ""  # 'var content' to add template variables
        return context
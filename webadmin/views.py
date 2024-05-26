from django.shortcuts import render
from django.http import HttpResponse
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

# ====================================
# Actores
# ====================================

class ActoresCreateView(CreateView):
    model = Actores
    template_name = "actor/add.html"

    fields = [
        'NombreActor'
    ]
 
    success_url = reverse_lazy('web_app:correcto')

    def form_valid(self, form):
        # Logica del Proceso
        actor = form.save(commit=False)
        actor.save()
        return super(ActoresCreateView, self).form_valid(form)


class SuccessView(TemplateView):
        template_name = "actor/success.html"

# ====================================        
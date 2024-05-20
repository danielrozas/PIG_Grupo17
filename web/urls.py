from django.urls import path
from . import views

urlpatterns = [
    # Cuando entre a localhost/ nada la vista que buscará será 
    # la que tiene el nombre index
    path('', views.index, name='index')
]
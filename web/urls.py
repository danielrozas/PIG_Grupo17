from django.urls import path, re_path

from . import views
from .views import eliminar_pelicula, modificar_pelicula

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),
    
    path('admin/', views.index_admin, name='admin'),
    path('admin/agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('admin/pelicula/<int:pelicula_id>/eliminar/', eliminar_pelicula, name='eliminar_pelicula'),
    path('admin/pelicula/<int:pelicula_id>/modificar/', modificar_pelicula, name='modificar_pelicula'),
    path('admin/lista_peliculas/', views.PeliculasListView.as_view(), name='lista_peliculas_admin'),
    path('admin/agregar_director/', views.agregar_director, name='agregar_director'),
    path('admin/agregar_genero/', views.agregar_genero, name='agregar_genero'),
    path('admin/lista_directores/', views.lista_directores, name='lista_directores'),
    path('admin/lista_generos/', views.lista_generos, name='lista_generos'),

]
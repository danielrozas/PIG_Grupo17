from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('pelicula/<int:pelicula_id>/eliminar/', views.eliminar_pelicula, name='eliminar_pelicula'),
    path('lista_peliculas/', views.PeliculasListView.as_view(), name='lista_peliculas_admin'),
    path('admin/', views.index_admin, name='admin'),
    path('agregar_director/', views.agregar_director, name='agregar_director'),
    path('agregar_genero/', views.agregar_genero, name='agregar_genero'),
    path('lista_directores/', views.lista_directores, name='lista_directores'),
    path('lista_generos/', views.lista_generos, name='lista_generos'),

]
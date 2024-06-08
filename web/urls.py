from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('pelicula/<int:pelicula_id>/eliminar/', views.eliminar_pelicula, name='eliminar_pelicula'),
    path('lista_peliculas/', views.lista_peliculas_admin, name='lista_peliculas_admin'),
    path('index_admin/', views.index_admin, name='index_admin'),

]
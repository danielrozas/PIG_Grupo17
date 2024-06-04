from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),

]
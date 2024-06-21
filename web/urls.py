from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views

from . import views
from .views import eliminar_pelicula, modificar_pelicula

urlpatterns = [
    path('', views.index, name='index'),

    #path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/login/", auth_views.LoginView.as_view(template_name="web/registration/login.html"), name="login"),
    #path("accounts/logout/", auth_views.LogoutView.as_view(template_name="web/registration/logout.html"), name="logout"),
    path("accounts/logout/", views.user_logout, name="logout"),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(template_name="web/registration/password_reset.html"), name="password_reset"),
    path('accounts/signup/', views.user_signup, name='signup'),
    
    path('peliculas/', views.listar_peliculas, name='listar_peliculas'),
    path('alquilar/<int:pelicula_id>/', views.alquilar_pelicula, name='alquilar_pelicula'),
    path('mis_peliculas/', views.lista_peliculas_alquiladas, name='lista_peliculas_alquiladas'),
    
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('pelicula/<int:pelicula_id>/eliminar/', eliminar_pelicula, name='eliminar_pelicula'),
    path('pelicula/<int:pelicula_id>/modificar/', modificar_pelicula, name='modificar_pelicula'),
    path('agregar_director/', views.agregar_director, name='agregar_director'),
    path('agregar_genero/', views.agregar_genero, name='agregar_genero'),
    path('lista_directores/', views.DirectoresListView.as_view(), name='lista_directores'),
    path('alquileres/', views.listar_alquileres, name='lista_alquileres'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('lista_generos/', views.GenerosListView.as_view(), name='lista_generos'),

]
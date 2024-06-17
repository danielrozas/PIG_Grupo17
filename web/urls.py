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
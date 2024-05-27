from django.urls import path, re_path
from . import views


app_name = "webadmin_app"

urlpatterns = [
    path('', 
        views.InicioView.as_view(), 
        name='index'),
    path('add-actor/', 
        views.ActorCreateView.as_view(),
        name='alta_actor'),
    path('mostrar-actor/<pk>/', 
        views.ActorDetailView.as_view(),
        name='mostrar_actor'),
    path('update-actor/<pk>/',
        views.ActorUpdateView.as_view(),
        name='modificar_actor'),
    path(
        'delete-actor/<pk>/',
        views.ActorDeleteView.as_view(),
        name='eliminar_actor'), 
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'),
    path('opciones-tabla', 
        views.OpcionesTablaView.as_view(), 
        name='opciones_tabla'),        
]
from django.urls import path, re_path
from . import views

app_name="web_app"

urlpatterns = [
    # Cuando entre a localhost/ nada la vista que buscará será 
    # la que tiene el nombre index
    # path('', views.index, name='index'),

    path('add-actor', views.ActoresCreateView.as_view(), name='agregar-actor'),

    path('success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),

    # path('saludar/<str:nombre>', views.saludar, name='saludar'),
    # re_path('^alumnos_por_anio/(?P<year>[0-9]{4})/$', views.alumnos_por_año, name='alumnos_por_anio'),
    # path('listado_alumnos', views.listado_alumnos, name='lista_alumnos')
]
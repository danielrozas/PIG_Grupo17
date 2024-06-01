from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cliente', views.ClienteDetailView.as_view(), name='cliente_detail'),


]
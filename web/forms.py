from django import forms
from .models import Peliculas
from django.core.exceptions import ValidationError
import datetime

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = ['TituloPelicula', 'Director_id', 'Genero_id', 'AnioLanzamiento', 'Duracion', 'PrecioAlquiler', 'Disponibilidad', 'URLCartel']

    def clean_AnioLanzamiento(self):
        anio_lanzamiento = self.cleaned_data.get('AnioLanzamiento')
        if anio_lanzamiento > datetime.datetime.now().year:
            raise ValidationError("El año de lanzamiento no puede estar en el futuro.")
        return anio_lanzamiento

    def clean_Duracion(self):
        duracion = self.cleaned_data.get('Duracion')
        if duracion <= 0:
            raise ValidationError("La duración debe ser un número positivo.")
        if duracion > 300:
            raise ValidationError("La duración no puede ser mayor a 300 minutos.")
        return duracion

    def clean_PrecioAlquiler(self):
        precio_alquiler = self.cleaned_data.get('PrecioAlquiler')
        if precio_alquiler <= 0:
            raise ValidationError("El precio de alquiler debe ser un valor positivo.")
        return precio_alquiler

    def clean(self):
        cleaned_data = super().clean()
        # agregar validaciones adicionales
        return cleaned_data
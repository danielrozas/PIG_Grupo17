from django import forms
from .models import Peliculas, Directores, Generos
from django.core.exceptions import ValidationError
import datetime

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Peliculas
        fields = '__all__'

    def clean_AnioLanzamiento(self):
        anio = self.cleaned_data.get('AnioLanzamiento')
        if anio is None:
            raise forms.ValidationError("Este campo es obligatorio.")
        if not isinstance(anio, int):
            raise forms.ValidationError("El año de lanzamiento debe ser un número entero.")
        if anio < 1900 or anio > 2100:
            raise forms.ValidationError("El año de lanzamiento debe estar entre 1900 y 2100.")
        return anio

    def clean_Duracion(self):
        duracion = self.cleaned_data.get('Duracion')
        if duracion is None:
            raise forms.ValidationError("Este campo es obligatorio.")
        if not isinstance(duracion, int):
            raise forms.ValidationError("La duración debe ser un número entero.")
        if duracion < 0 or duracion > 300:
            raise forms.ValidationError("La duración debe estar entre 0 y 300 minutos.")
        return duracion

    def clean_PrecioAlquiler(self):
        precio_alquiler = self.cleaned_data.get('PrecioAlquiler')
        if precio_alquiler is None:
            raise forms.ValidationError("Este campo es obligatorio.")
        try:
            precio_alquiler = float(precio_alquiler)
        except (TypeError, ValueError):
            raise forms.ValidationError("El precio de alquiler debe ser un número válido.")

        if precio_alquiler < 0:
            raise forms.ValidationError("El precio de alquiler no puede ser negativo.")
        return precio_alquiler
    
    def clean_URLCartel(self):
        url_cartel = self.cleaned_data.get('URLCartel')
        
        if not url_cartel:
            raise forms.ValidationError("Debe cargar una imagen para el poster.")

        return url_cartel

    def clean(self):
        cleaned_data = super().clean()
        # agregar validaciones adicionales
        return cleaned_data

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Directores
        fields = ['NombreDirector']

    def clean_NombreDirector(self):
        nombre_director = self.cleaned_data.get('NombreDirector')
        if Directores.objects.filter(NombreDirector=nombre_director).exists():
            raise forms.ValidationError("Este director ya existe.")
        return nombre_director

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Generos
        fields = ['DescripcionGenero']

    def clean_DescripcionGenero(self):
        descripcion_genero = self.cleaned_data.get('DescripcionGenero')
        if Generos.objects.filter(DescripcionGenero=descripcion_genero).exists():
            raise forms.ValidationError("Este género ya existe.")
        return descripcion_genero

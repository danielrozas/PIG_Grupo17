from django import forms
from .models import Peliculas, Directores, Generos, Clientes, Alquiler
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField  
from django.forms.forms import Form
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
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
        cantidad_disponible = cleaned_data.get("CantidadDisponible")
        
        if cantidad_disponible is not None:
            cleaned_data["Disponibilidad"] = cantidad_disponible > 0
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

class SignupForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', min_length=5, max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    direccion = forms.CharField(max_length=45, required=True, label="Dirección")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'direccion']

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya existe.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email ya existe.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class AlquilerForm(forms.ModelForm):
    class Meta:
        model = Alquiler
        fields = ['FechaFin']
        labels = {
            'FechaFin': 'Fecha de Finalización',
        }
        widgets = {
            'FechaFin': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/YYYY'}),
        }

    def clean_FechaFin(self):
        fecha_fin = self.cleaned_data.get('FechaFin')
        if fecha_fin < timezone.now().date():
            raise forms.ValidationError("La fecha de finalización no puede ser en el pasado.")
        return fecha_fin
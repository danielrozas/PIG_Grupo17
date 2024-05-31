from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Clientes(models.Model):
    NombreCliente = models.CharField(max_length=60, verbose_name="NombreCliente")
    Email =models.EmailField(max_length=45, verbose_name="Email")
    Direccion =  models.CharField(max_length=45, verbose_name="Direccion")

class Directores(models.Model):
    NombreDirector = models.CharField(max_length=60, verbose_name="NombreDirector")

class Generos(models.Model):
    DescripcionGenero = models.CharField(max_length=60, verbose_name="DescripcionGenero")

class Peliculas(models.Model):
    TituloPelicula = models.CharField(max_length=128, verbose_name="TituloPelicula") 
    Director_id = models.ForeignKey(Directores, on_delete=models.CASCADE)
    Genero_id = models.ForeignKey(Generos, on_delete=models.CASCADE)
    AnioLanzamiento = models.IntegerField(verbose_name="AnioLanzamiento",
                validators=[MinValueValidator(1900),
                            MaxValueValidator(2100)])
    Duracion = models.IntegerField(verbose_name="Duracion",
                validators=[MinValueValidator(0),
                            MaxValueValidator(300)])
    PrecioAlquiler = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="PrecioAlquiler")
    Disponibilidad = models.BooleanField(verbose_name="Disponibilidad")
    URLCartel = models.CharField(max_length=150, verbose_name="URLCartel")

class Alquiler(models.Model):
    Pelicula_id = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    Cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)  
    FechaInicio = models.DateField(verbose_name="FechaInicio")
    FechaFin = models.DateField(verbose_name="FechaFin")
    PrecioTotal = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="PrecioTotal")
    Estado = models.BooleanField(verbose_name="Estado")


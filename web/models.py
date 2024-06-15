from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIG_Grupo17 import settings

# Create your models here.

class Clientes(models.Model):
    """
        https://stackoverflow.com/questions/71423191/django-user-model-with-same-fields

        para ver el objeto models.User
        https://docs.djangoproject.com/en/5.0/ref/contrib/auth/
    """
    user = models.OneToOneField(
          settings.AUTH_USER_MODEL,
          on_delete=models.CASCADE,
          null=True,
          blank=True
     )
    Direccion =  models.CharField(max_length=45, verbose_name="Direccion")

    # Este metodo provee una representaacion leible por una persona
    # de la instancia del modelo. Es particularmente util cuando se trabaja 
    # con la interface admin de Django
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} | Email: {self.user.email} | Dirección: {self.Direccion}"

class Directores(models.Model):
    NombreDirector = models.CharField(max_length=60, verbose_name="Director")

    def __str__(self):
        return self.NombreDirector

class Generos(models.Model):
    DescripcionGenero = models.CharField(max_length=60, verbose_name="Género")

    def __str__(self):
        return self.DescripcionGenero

class Peliculas(models.Model):
    TituloPelicula = models.CharField(max_length=128, verbose_name="Título") 
    Director = models.ForeignKey(Directores, on_delete=models.CASCADE)
    Genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    AnioLanzamiento = models.IntegerField(verbose_name="Año de Lanzamiento",
                validators=[MinValueValidator(1900),
                            MaxValueValidator(2100)])
    Duracion = models.IntegerField(verbose_name="Duración",
                validators=[MinValueValidator(0),
                            MaxValueValidator(300)])
    PrecioAlquiler = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Precio Alquiler")
    Disponibilidad = models.BooleanField(verbose_name="Disponibilidad")
    URLCartel = models.ImageField(upload_to='carteles/', verbose_name="Poster")

    def __str__(self):
        return f"{self.TituloPelicula} | Año de Lanzamiento {self.AnioLanzamiento} | Duración: {self.Duracion} minutos"    
class Alquiler(models.Model):
    Pelicula_id = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    Cliente_id = models.ForeignKey(Clientes, on_delete=models.CASCADE)  
    FechaInicio = models.DateField(verbose_name="Fecha de Inicio")
    FechaFin = models.DateField(verbose_name="Fecha de Finalización")
    PrecioTotal = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Precio Total")
    Estado = models.BooleanField(verbose_name="Estado")


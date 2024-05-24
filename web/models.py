from django.db import models

# Create your models here.


class Administradores(models.Model):
    idAdministrador = models.AutoField(primary_key=True) # Esto equivale a INTEGER UNSIGNED NOT NULL
    NombreAdministrador = models.CharField(max_length=60, null = False)
    ContrasenaAdministrador =models.CharField(max_length=20, null = False)

    def __str__(self):
        return self.NombreAdministrador
        
class Actores(models.Model):
    idActor = models.AutoField(primary_key=True) # Esto equivale a INTEGER UNSIGNED NOT NULL
    NombreActor = models.CharField(max_length=60, null = False)

    def __str__(self):
        return self.NombreActor

class Directores(models.Model):
    idDirector = models.AutoField(primary_key=True) # Esto equivale a INTEGER UNSIGNED NOT NULL
    NombreDirector = models.CharField(max_length=60, null = False)

    def __str__(self):
        return self.NombreDirector

class Peliculas(models.Model):
    idPelicula = models.AutoField(primary_key=True) # Esto equivale a INTEGER UNSIGNED NOT NULL
    NombrePelicula = models.CharField(max_length=128, null = False) 
    Director_id = models.ForeignKey(Directores, on_delete=models.CASCADE)
    FechaEstreno = models.DateTimeField(blank=True, null=True)
    URLCartel = models.CharField(max_length=150, null = True)

    def __str__(self):
        return self.NombrePelicula

class ActoresenPeliculas(models.Model):
    idActoresenPeliculas = models.AutoField(primary_key=True) # Esto equivale a INTEGER UNSIGNED NOT NULL
    Actor_id = models.ForeignKey(Actores, on_delete=models.CASCADE)    
    Pelicula_id = models.ForeignKey(Peliculas, on_delete=models.CASCADE)
    Papel = models.CharField(max_length=128, null = False)

    def __str__(self):
        return f"{self.Actor_id} {self.Pelicula_id}"
 
        return f"{self.Actor_id} {self.Pelicula_id}"
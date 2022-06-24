from django.db import models
from django.forms import CharField

# Create your models here.
class Usuario(models.Model):
  Nombre= models.CharField(max_length=30)
  Apellido= models.CharField(max_length=30)
  Email=models.EmailField()
  Pais=models.CharField(max_length=30)
  Edad=models.IntegerField()

class Categoria(models.Model):

  Rubro = models.CharField(max_length=50)
  Descripcion = models.CharField(max_length=200)

class Publicacion(Categoria):

  Titulo = models.CharField(max_length=60)
  Texto = models.CharField(max_length=500)













from django.db import models

# Create your models here.

class Categoria(models.Model):

  Nombre = models.CharField(max_length=50)
  Descripcion = models.CharField(max_length=200)

class Publicacion(Categoria):

  Titulo = models.CharField(max_length=60)
  Texto = models.CharField(max_length=500)







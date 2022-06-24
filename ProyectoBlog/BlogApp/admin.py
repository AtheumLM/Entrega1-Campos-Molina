from django.contrib import admin
from BlogApp.models import *

# Register your models here.

class categoriaAdmin(admin.ModelAdmin):

  list_display = ("Nombre","Descripcion")

admin.site.register(Categoria,categoriaAdmin)

class publicacionAdmin(admin.ModelAdmin):

  list_display = ("Titulo","Descripcion")

admin.site.register(Publicacion,publicacionAdmin)
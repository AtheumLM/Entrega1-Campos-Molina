from django.contrib import admin
from BlogApp.models import *

# Register your models here.

class categoriaAdmin(admin.ModelAdmin):

  list_display = ("Rubro","Descripcion")

admin.site.register(Categoria,categoriaAdmin)

class publicacionAdmin(admin.ModelAdmin):

  list_display = ("Titulo","Texto")

admin.site.register(Publicacion,publicacionAdmin)

class usuarioAdmin(admin.ModelAdmin):

  list_display = ("Nombre","Apellido","Email","Pais","Edad")

admin.site.register(Usuario,usuarioAdmin)

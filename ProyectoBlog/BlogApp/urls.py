from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("inicio", views.inicio, name="inicio"),
    path("categorias", views.categorias, name="categorias"),
    path("crear_categoria",views.crear_categoria, name="crear_categoria"),
    path("buscar_categoria",views.buscar_categoria, name="buscar_categoria"),
    path("usuarios",views.usuarios, name="usuarios"),
    path("crear_usuario",views.crear_usuario, name="crear_usuario"),
    path("buscar_usuario",views.buscar_usuario, name="buscar_usuario"),
    path("publicaciones", views.publicaciones, name="publicaciones"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("contacto", views.contacto, name="contacto"),
    
    
]

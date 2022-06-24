from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("categorias", views.categorias, name="categorias"),
    path("publicaciones", views.publicaciones, name="publicaciones"),
    
]

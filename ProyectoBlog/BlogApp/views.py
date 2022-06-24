from django.shortcuts import render
from django.http import HttpResponse
from BlogApp.models import *

# Create your views here.

def inicio(request):
  return render(request,"BlogApp/inicio.html")

def noticias(request):
  return render(request,"BlogApp/noticias.html")

def crearCategoria(request):

  nombre = "Steam,"

  descripcion = "Novedades sobre plataforma Steam"

  nuevaCategoria = Categoria(Nombre = nombre, Descripcion = descripcion)
  nuevaCategoria.save()

def publicaciones(request):
  return render(request,"BlogApp/publicaciones.html")

def nosotros(request):
  return render(request,"BlogApp/nosotros.html")

def contacto(request):
  return render(request,"BlogApp/contacto.html")



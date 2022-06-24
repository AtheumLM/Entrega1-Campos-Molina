from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
  return render(request,"BlogApp/inicio.html")

def noticias(request):
  return render(request,"BlogApp/categorias.html")

def publicaciones(request):
  return render(request,"BlogApp/publicaciones.html")

def nosotros(request):
  return render(request,"BlogApp/nosotros.html")

def contacto(request):
  return render(request,"BlogApp/contacto.html")



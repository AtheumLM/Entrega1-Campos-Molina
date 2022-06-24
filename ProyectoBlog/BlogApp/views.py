from django.shortcuts import render
from django.http import HttpResponse
from BlogApp.models import *

# Create your views here.

def inicio(request):
  return render(request,"BlogApp/inicio.html")

def categorias(request):

  cat = Categorias.objects.all()

  return render(request,"BlogApp/categorias.html",{"Categorias": cat})

def publicaciones(request):
  return render(request,"BlogApp/publicaciones.html")

def nosotros(request):
  return render(request,"BlogApp/nosotros.html")

def contacto(request):
  return render(request,"BlogApp/contacto.html")



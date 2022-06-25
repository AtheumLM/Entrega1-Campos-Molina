from django.shortcuts import redirect, render
from django.http import HttpResponse
from BlogApp.models import *
from .forms import Crear_Categoria

# Create your views here.

def inicio(request):
  return render(request,"BlogApp/inicio.html")

def categorias(request):

  cat = Categorias.objects.all()

  return render(request,"BlogApp/categorias.html",{"Categorias": cat})

def crear_categoria(request):
  if request.method=='POST':
    categoria_formulario= Crear_Categoria(request.POST)
    print(categoria_formulario)


    if categoria_formulario .is_valid():
      info=categoria_formulario.cleaned_data
      categoria_creada= Categorias (Rubro=info['Rubro'], Descripcion=info['Descripcion'],)
      categoria_creada.save()
      return redirect("categorias")


  categoria_formulario= Crear_Categoria()
  print(categoria_formulario)

  return render(request,"BlogApp/crear_categoria.html",{'form':categoria_formulario})


def buscar_categoria(request):
  
  if request.method=='POST':
    Rubro=request.POST["Rubro"]
    Rubros=Categorias.objects.filter(Rubro__icontains=Rubro)
    return render(request,"BlogApp/buscar_categoria.html",{'Rubros':Rubros})
  
  else:

    Rubro=[]
    return render(request,"BlogApp/buscar_categoria.html",{'Rubro':Rubro})



def publicaciones(request):
  return render(request,"BlogApp/publicaciones.html")

def nosotros(request):
  return render(request,"BlogApp/nosotros.html")

def contacto(request):
  return render(request,"BlogApp/contacto.html")



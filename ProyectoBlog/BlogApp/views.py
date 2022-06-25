from django.shortcuts import redirect, render
from django.http import HttpResponse
from BlogApp.models import *
from .forms import *
from django.db.models import Q


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
    Rubros=Categorias.objects.filter( Q(Rubro__icontains=Rubro) | Q(Descripcion__icontains=Rubro)).values()
    return render(request,"BlogApp/buscar_categoria.html",{'Rubros':Rubros})
  
  else:

    Rubro=[]
    return render(request,"BlogApp/buscar_categoria.html",{'Rubro':Rubro})

def usuarios(request):

  usu = Usuario.objects.all()
  return render(request,"BlogApp/usuarios.html",{"Usuarios": usu})

def crear_usuario(request):
  if request.method=='POST':
    usuario_formulario=Crear_Usuario(request.POST)
    print(usuario_formulario)

    if usuario_formulario.is_valid():
      info=usuario_formulario.cleaned_data
      usuario_creado= Usuario (Nombre=info['Nombre'], Apellido=info['Apellido'],Email=info['Email'],Pais=info['Pais'],Edad=info['Edad'],)
      usuario_creado.save()
      return redirect("usuarios")

  usuario_formulario= Crear_Usuario()
  print(usuario_formulario)
  return render(request,"BlogApp/crear_usuario.html",{'form':usuario_formulario}) 

def buscar_usuario(request):

  if request.method=='POST':
    Nombre=request.POST["Nombre"]
    Nombres=Usuario.objects.filter( Q(Nombre__icontains=Nombre) | Q(Apellido__icontains=Nombre)).values()
    return render(request,"BlogApp/buscar_usuario.html",{'Nombres': Nombres})
  
  else:

    Nombre=[]
    return render(request,"BlogApp/buscar_usuario.html",{'Nombre':Nombre})




def publicaciones(request):
  pub=Publicacion.objects.all()
  return render(request,"BlogApp/publicaciones.html",{'Publicaciones':pub})

def crear_publicacion(request):

  if request.method=='POST':
    publicacion_formulario=Crear_Publicacion(request.POST)
    print(publicacion_formulario)

    if publicacion_formulario.is_valid():
      info=publicacion_formulario.cleaned_data
      publicacion_creada=Publicacion(Titulo=info['Titulo'],Texto=info['Texto'])
      publicacion_creada.save()
      return redirect("publicaciones")
  
  publicacion_formulario= Crear_Publicacion()
  print(publicacion_formulario)
  return render(request,"BlogApp/crear_publicaciones.html",{'form':publicacion_formulario}) 


def buscar_publicacion(request):
    if request.method=='POST':
      Titulo=request.POST["Titulo"]
      Titulos=Publicacion.objects.filter(Titulo__icontains=Titulo).values()
      return render(request,"BlogApp/buscar_publicacion.html",{'Titulos': Titulos})
  
    else:

      Titulo=[]
      return render(request,"BlogApp/buscar_publicacion.html",{'Titulo':Titulo})


def nosotros(request):
  return render(request,"BlogApp/nosotros.html")

def contacto(request):
  return render(request,"BlogApp/contacto.html")



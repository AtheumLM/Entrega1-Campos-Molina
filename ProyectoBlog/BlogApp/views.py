from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
  return render(request,"BlogApp/index.html")

def categorias(request):
  return render(request,"BlogApp/index.html")

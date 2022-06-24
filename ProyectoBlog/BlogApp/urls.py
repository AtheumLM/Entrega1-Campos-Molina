from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("inicio", views.inicio, name="inicio"),
    path("noticias", views.noticias, name="noticias"),
    path("publicaciones", views.publicaciones, name="publicaciones"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("contacto", views.contacto, name="contacto"),
    
    
]

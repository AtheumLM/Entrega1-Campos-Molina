from django import forms

class Crear_Categoria(forms.Form):
    Rubro=forms.CharField(max_length=50)
    Descripcion = forms.CharField(max_length=200)

class Crear_Usuario(forms.Form):
    Nombre= forms.CharField(max_length=30)
    Apellido= forms.CharField(max_length=30)
    Email=forms.EmailField()
    Pais=forms.CharField(max_length=30)
    Edad=forms.IntegerField()
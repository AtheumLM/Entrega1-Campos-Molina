from django import forms

class Crear_Categoria(forms.Form):
    Rubro=forms.CharField(max_length=50)
    Descripcion = forms.CharField(max_length=200)
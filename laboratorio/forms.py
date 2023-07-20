from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Ingrese el nombre del Laboratorio'}))
    ciudad = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Ingrese la ciudad del Laboratorio'}))
    pais = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Ingrese el pais del Laboratorio'}))

    class Meta: 
        model = Laboratorio
        fields = "__all__"

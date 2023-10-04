from django import forms


class AlumnosFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    email = forms.EmailField()

class ClasesFormulario(forms.Form):
    tipo = forms.CharField(max_length=40)
    dia = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type' : 'date'}))
    tiempo = forms.IntegerField()

class SucursalesFormulario(forms.Form):
    ciudad = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    calle = forms.IntegerField()
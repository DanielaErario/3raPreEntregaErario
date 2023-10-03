from django.shortcuts import render
from django.http import HttpResponse
from .models import Alumno,Clase,Sucursal
# Create your views here.

def inicio(request):
    return HttpResponse("Hola culo roto")

def alumnos(request):
    return render(request, "AppGimnasio/alumnos.html")

def clases(request):
    return render(request, "AppGimnasio/clases.html")

def sucursales(request):
    return render(request, "AppGimnasio/sucursales.html")




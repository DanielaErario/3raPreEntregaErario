from django.shortcuts import render
from django.http import HttpResponse
from .models import Alumno,Clase,Sucursal
from AppGimnasio.forms import AlumnosFormulario
# Create your views here.

def inicio(request):
    return render(request, "AppGimnasio/index.html")

def alumnos(request):
    return render(request, "AppGimnasio/alumnos.html")

def clases(request):
    return render(request, "AppGimnasio/clases.html")

def sucursales(request):
    return render(request, "AppGimnasio/sucursales.html")

def alumnosFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = AlumnosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Alumno(nombre=informacion["nombre"], apellido=informacion["apellido"],edad=informacion["edad"],email=informacion["email"])
                  curso.save()
                  return render(request, "AppGimnasio/index.html")
      else:
            miFormulario = AlumnosFormulario()
 
      return render(request, "AppGimnasio/alumnosFormulario.html", {"miFormulario": miFormulario})




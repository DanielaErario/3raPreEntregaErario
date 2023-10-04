from django.shortcuts import render
from django.http import HttpResponse
from .models import Alumno,Clase,Sucursal
from AppGimnasio.forms import AlumnosFormulario, ClasesFormulario, SucursalesFormulario
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

def clasesFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = ClasesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  clase = Clase(clase=informacion["clase"], dia=informacion["dia"],duracion=informacion["duracion"])
                  clase.save()
                  return render(request, "AppGimnasio/index.html")
      else:
            miFormulario = ClasesFormulario()
 
      return render(request, "AppGimnasio/clasesFormulario.html", {"miFormulario": miFormulario})

def sucursalesFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = SucursalesFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  sucursal = Sucursal(ciudad=informacion["ciudad"], direccion=informacion["direccion"],calle=informacion["calle"])
                  sucursal.save()
                  return render(request, "AppGimnasio/index.html")
      else:
            miFormulario = ClasesFormulario()
 
      return render(request, "AppGimnasio/sucursalesFormulario.html", {"miFormulario": miFormulario})


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
                  datos = Alumno(nombre=informacion["nombre"], apellido=informacion["apellido"],edad=informacion["edad"],email=informacion["email"])
                  datos.save()
                  return render(request, "AppGimnasio/index.html")
      else:
            miFormulario = AlumnosFormulario()
 
      return render(request, "AppGimnasio/alumnosFormulario.html", {"miFormulario": miFormulario})

def clasesFormulario(request):
 
      if request.method == "POST":
 
            FormularioDos = ClasesFormulario(request.POST) # Aqui me llega la informacion del html
            print(FormularioDos)
 
            if FormularioDos.is_valid:
                  informacion = FormularioDos.cleaned_data
                  clase = Clase(tipo=informacion["tipo"], dia=informacion["dia"],tiempo=informacion["tiempo"])
                  clase.save()
                  return render(request, "AppGimnasio/index.html")
      else:
            FormularioDos = ClasesFormulario()
 
      return render(request, "AppGimnasio/clasesFormulario.html", {"FormularioDos": FormularioDos})

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

def busquedaAlumno(request):
      return render(request, "AppGimnasio/busquedaAlumno.html")

def buscar(request):
      if request.GET['apellido'] or request.GET['nombre']:
            nombre = request.GET['nombre']
            apellido = request.GET['apellido']
            email = Alumno.objects.filter(nombre__icontains=apellido)
            return render(request, "AppGimnasio/resultadosBusqueda.html", {"nombre":nombre, "apellido":apellido})
      else:
            respuesta = "No enviaste datos"

      return HttpResponse(respuesta)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Alumno,Clase,Sucursal
from AppGimnasio.forms import AlumnosFormulario, ClasesFormulario, SucursalesFormulario
# Create your views here.

def inicio(request):
    return render(request, "AppGimnasio/index.html")

def alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, "AppGimnasio/alumnos.html",{"alumnos":alumnos})

def clases(request):
    clases = Clase.objects.all()
    return render(request, "AppGimnasio/clases.html",{"clases":clases})

def sucursales(request):
    sucursales = Sucursal.objects.all()
    return render(request, "AppGimnasio/sucursales.html",{"sucursales":sucursales})

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
                  datos = Clase(clase=informacion["clase"], dia=informacion["dia"],tiempo=informacion["tiempo"])
                  datos.save()
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
      if request.GET["apellido"]:
            apellido = request.GET["apellido"]
            alumnos = Alumno.objects.filter(apellido__icontains=apellido)
            return render(request, "AppGimnasio/resultadosBusqueda.html", {"alumnos":alumnos, "apellido":apellido})
      else:
            respuesta = "No enviaste datos"

      return HttpResponse(respuesta)
      
      
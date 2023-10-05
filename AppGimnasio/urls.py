from django.urls import path
from AppGimnasio import views

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('alumnos/', views.alumnos, name = "Alumnos"),
    path('clases/', views.clases, name = "Clases"),
    path('sucursales/', views.sucursales, name = "Sucursales"),
    path('alumnosFormulario/', views.alumnosFormulario, name = "AlumnosFormulario"),
    path('clasesFormulario/', views.clasesFormulario, name = "ClasesFormulario"),
    path('sucursalesFormulario/', views.sucursalesFormulario, name = "SucursalesFormulario"),
    path('busquedaAlumno/', views.busquedaAlumno, name= "busquedaAlumno"),
    path('buscar/', views.buscar),
   
]


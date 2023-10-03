from django.urls import path
from AppGimnasio import views

urlpatterns = [
    path('', views.inicio, name = "Inicio"),
    path('alumnos/', views.alumnos, name = "Alumnos"),
    path('clases/', views.clases, name = "Clases"),
    path('sucursales/', views.sucursales, name = "Sucursales"),
    path('alumnosFormulario/', views.alumnosFormulario, name = "alumnosFormulario")
   
]


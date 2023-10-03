from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()

class Clase(models.Model):
    nombre = models.CharField(max_length=40)
    dia = models.IntegerField()
    horario = models.DateField()
    

class Sucursal(models.Model):
    ciudad = models.CharField(max_length=40)
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()


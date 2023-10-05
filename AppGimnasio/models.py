from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self): #Esta funcion con __str__ es para que el panel se vea mas lindo.
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Edad {self.edad} - E-Mail {self.email}"


class Clase(models.Model):
    clase = models.CharField(max_length=40)
    dia = models.DateField()
    tiempo = models.IntegerField()
    def __str__(self):
        return f"Clase: {self.clase} - Dia {self.dia} - Tiempo {self.tiempo}"

class Sucursal(models.Model):
    ciudad = models.CharField(max_length=40)
    calle = models.CharField(max_length=20)
    numero = models.IntegerField()
    def __str__(self):
        return f"Ciudad: {self.ciudad} - Calle {self.calle} - Numero {self.numero}"


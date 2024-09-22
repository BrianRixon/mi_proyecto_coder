from django.db import models

# Create your models here.

class Registro(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'



class Productos(models.Model):
    producto = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return (self.producto)

class Turnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    fecha = models.DateTimeField()    

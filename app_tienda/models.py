from django.db import models

# Create your models here.

class Registro(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField(max_length=10)
    email = models.EmailField()



class Productos(models.Model):
    producto = models.CharField(max_length=50)
    rubro = models.CharField(max_length=50)


class Turnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento = models.IntegerField()
    fecha = models.DateTimeField()    

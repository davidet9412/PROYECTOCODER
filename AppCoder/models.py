from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision= models.IntegerField()

    def __str__(self):
        return self.nombre+"" + str(self.comision)
class Estudiantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.nombre+" "+ self.apellido

class Profesores(models.Model):
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+ self.apellido + "cuya profesión es: " + self.profesion

class Entregables(models.Model):
    nombre= models.CharField(max_length=50)    
    fecha_entrega=models.DateField()
    entregado = models.BooleanField()


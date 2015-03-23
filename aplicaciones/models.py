from django.db import models

class Aplicacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
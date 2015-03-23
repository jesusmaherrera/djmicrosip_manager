from django.db import models
from aplicaciones.models import Aplicacion

class AppRelease(models.Model):
    aplicacion = models.ForeignKey(Aplicacion)
    version = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
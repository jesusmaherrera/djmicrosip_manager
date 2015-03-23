from django.db import models
from clientes.models import Cliente
from app_releases.models import AppRelease

class Installation(models.Model):
    cliente = models.ForeignKey(Cliente)
    fecha = models.DateTimeField()

class AppInstalation(models.Model):
    installation = models.ForeignKey(Installation)
    app_release = models.ForeignKey(AppRelease)

from django.db import models
from clients.models import Client
from applications.models import Application

class ClientApplication(models.Model):
    client = models.ForeignKey(Client)
    application =  models.ForeignKey(Application)
    version = models.CharField(max_length=50)

    def __unicode__(self):
        return '%s-%s v%s'%(self.client.user.username, self.application.name, self.version)
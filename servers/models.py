from django.db import models
from clients.models import Client

class Server(models.Model):
    client = models.ForeignKey(Client, unique=True)
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    mac_address = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s-%s'%(self.client.user.username, self.mac_address)
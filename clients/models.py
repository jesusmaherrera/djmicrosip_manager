from django.db import models
from django.contrib.auth.models import User
from companies.models import Company

class Client(models.Model):
    name = models.CharField(max_length=200)
    # user = models.ForeignKey(User, unique=True)
    # company =  models.ForeignKey(Company)

    def __unicode__(self):
        return self.name
    
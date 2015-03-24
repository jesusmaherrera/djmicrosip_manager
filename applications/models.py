from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
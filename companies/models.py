from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=200)
    rfc = models.CharField(max_length=13)

    def __unicode__(self):
        return u'%s' % self.name
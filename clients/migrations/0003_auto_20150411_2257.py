# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0002_auto_20150407_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='company',
            field=models.ForeignKey(default=2, to='companies.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=50)),
                ('application', models.ForeignKey(to='applications.Application')),
                ('client', models.ForeignKey(to='clients.Client', unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

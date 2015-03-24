# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientapplications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientapplication',
            name='client',
            field=models.ForeignKey(to='clients.Client'),
            preserve_default=True,
        ),
    ]

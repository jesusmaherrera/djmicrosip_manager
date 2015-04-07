# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='company',
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 4, 7, 18, 37, 12, 952000, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]

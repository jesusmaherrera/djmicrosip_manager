# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_releases', '0001_initial'),
        ('clientes', '0001_initial'),
        ('instalaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppInstalation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_release', models.ForeignKey(to='app_releases.AppRelease')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('cliente', models.ForeignKey(to='clientes.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='installacion',
            name='aplicacion',
        ),
        migrations.RemoveField(
            model_name='installacion',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Installacion',
        ),
        migrations.AddField(
            model_name='appinstalation',
            name='installation',
            field=models.ForeignKey(to='instalaciones.Installation'),
            preserve_default=True,
        ),
    ]

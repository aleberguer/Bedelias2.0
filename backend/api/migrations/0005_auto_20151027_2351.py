# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20151027_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='facultad',
            field=models.ForeignKey(related_name='carreras', blank=True, to='api.Facultad', null=True),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='nombre',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]

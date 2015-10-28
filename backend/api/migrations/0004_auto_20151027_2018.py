# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151027_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='aprobacion',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'curso', b'Curso'), (b'examen', b'Examen')]),
        ),
    ]

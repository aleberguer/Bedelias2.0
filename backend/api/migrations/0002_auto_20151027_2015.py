# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='carrera',
            field=models.ForeignKey(blank=True, to='api.Carrera', null=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='creditos',
            field=models.IntegerField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151027_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='creditos',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='validez',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

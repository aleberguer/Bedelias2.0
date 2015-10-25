# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151025_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='antiprevias',
            field=models.ManyToManyField(related_name='_antiprevias_+', null=True, to='api.Curso', blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='previas_curso',
            field=models.ManyToManyField(related_name='_previas_curso_+', null=True, to='api.Curso', blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='previas_grupo',
            field=models.ManyToManyField(to='api.Grupo', null=True, blank=True),
        ),
    ]

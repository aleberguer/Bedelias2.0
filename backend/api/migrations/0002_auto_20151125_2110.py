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
            name='antiprevias_curso_tipoCurso',
            field=models.ManyToManyField(related_name='anti_cursos_curso', to='api.Curso', blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='antiprevias_examen_tipoCurso',
            field=models.ManyToManyField(related_name='anti_examenes_curso', to='api.Curso', blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='previas_curso_tipoCurso',
            field=models.ManyToManyField(to='api.Curso', blank=True),
        ),
        migrations.AlterField(
            model_name='curso',
            name='previas_examen_tipoCurso',
            field=models.ManyToManyField(related_name='examenes_grupo', to='api.Curso', blank=True),
        ),
    ]

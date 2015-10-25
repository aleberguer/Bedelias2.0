# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_usuario_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('aprobacion', models.CharField(max_length=200, choices=[(b'curso', b'Curso'), (b'examen', b'Examen')])),
                ('validez', models.IntegerField()),
                ('creditos', models.IntegerField()),
                ('antiprevias', models.ManyToManyField(related_name='_antiprevias_+', to='api.Curso')),
                ('previas_curso', models.ManyToManyField(related_name='_previas_curso_+', to='api.Curso')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('puntaje_minimo', models.IntegerField()),
                ('puntaje_maximo', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GrupoCurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntaje_minimo', models.IntegerField()),
                ('curso', models.ForeignKey(to='api.Curso')),
                ('grupo', models.ForeignKey(to='api.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioCurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=200, choices=[(b'curso_aprobado', b'Curso aprobado'), (b'examen_aprobado', b'Examen Aprobado')])),
                ('curso', models.ForeignKey(to='api.Curso')),
                ('usuario', models.ForeignKey(to='api.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='grupo',
            name='cursos',
            field=models.ManyToManyField(to='api.Curso', through='api.GrupoCurso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='previas_grupo',
            field=models.ManyToManyField(to='api.Grupo'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='cursos',
            field=models.ManyToManyField(to='api.Curso', through='api.UsuarioCurso'),
        ),
    ]

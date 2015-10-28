# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('nombre', models.CharField(max_length=200)),
                ('codigo', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('plan', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=200)),
                ('aprobacion', models.CharField(max_length=200, choices=[(b'curso', b'Curso'), (b'examen', b'Examen')])),
                ('validez', models.IntegerField()),
                ('creditos', models.IntegerField()),
                ('antiprevias', models.ManyToManyField(related_name='_antiprevias_+', to='api.Curso', blank=True)),
                ('carrera', models.ForeignKey(to='api.Carrera', null=True)),
                ('previas_curso', models.ManyToManyField(related_name='_previas_curso_+', to='api.Curso', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=128)),
                ('puntaje_minimo', models.IntegerField()),
                ('puntaje_maximo', models.IntegerField()),
            ],
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
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('carrera', models.ForeignKey(blank=True, to='api.Carrera', null=True)),
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
            model_name='usuario',
            name='cursos',
            field=models.ManyToManyField(to='api.Curso', through='api.UsuarioCurso'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grupo',
            name='cursos',
            field=models.ManyToManyField(to='api.Curso', through='api.GrupoCurso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='previas_grupo',
            field=models.ManyToManyField(to='api.Grupo', blank=True),
        ),
        migrations.AddField(
            model_name='carrera',
            name='facultad',
            field=models.ForeignKey(related_name='carreras', to='api.Facultad', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together=set([('codigo', 'carrera')]),
        ),
    ]

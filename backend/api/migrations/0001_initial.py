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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200, null=True, blank=True)),
                ('codigo', models.CharField(max_length=20)),
                ('plan', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=200)),
                ('aprobacion', models.CharField(blank=True, max_length=200, null=True, choices=[(b'curso', b'Curso'), (b'examen', b'Examen')])),
                ('validez', models.IntegerField(null=True, blank=True)),
                ('creditos', models.IntegerField(null=True, blank=True)),
                ('antiprevias_curso_tipoCurso', models.ManyToManyField(related_name='_antiprevias_curso_tipoCurso_+', to='api.Curso', blank=True)),
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
                ('codigo', models.CharField(max_length=128)),
                ('puntaje_minimo', models.IntegerField()),
                ('puntaje_maximo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GrupoCurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('puntaje', models.IntegerField()),
                ('actividad', models.CharField(max_length=200, choices=[(b'curso_aprobado', b'Curso aprobado'), (b'examen_aprobado', b'Examen Aprobado')])),
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
            field=models.ManyToManyField(to='api.Curso', through='api.GrupoCurso', blank=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='facultad',
            field=models.ForeignKey(blank=True, to='api.Facultad', null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='antiprevias_curso_tipoGrupo',
            field=models.ManyToManyField(related_name='anti_cursos', to='api.Grupo', blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='antiprevias_examen_tipoCurso',
            field=models.ManyToManyField(related_name='_antiprevias_examen_tipoCurso_+', to='api.Curso', blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='antiprevias_examen_tipoGrupo',
            field=models.ManyToManyField(related_name='anti_examenes', to='api.Grupo', blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='carrera',
            field=models.ForeignKey(blank=True, to='api.Carrera', null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='facultad',
            field=models.ForeignKey(blank=True, to='api.Facultad', null=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='previas_curso_tipoCurso',
            field=models.ManyToManyField(related_name='_previas_curso_tipoCurso_+', to='api.Curso', blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='previas_curso_tipoGrupo',
            field=models.ManyToManyField(to='api.Grupo', blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='previas_examen_tipoCurso',
            field=models.ManyToManyField(related_name='_previas_examen_tipoCurso_+', to='api.Curso', blank=True),
        ),
        migrations.AddField(
            model_name='curso',
            name='previas_examen_tipoGrupo',
            field=models.ManyToManyField(related_name='examenes_curso', to='api.Grupo', blank=True),
        ),
        migrations.AddField(
            model_name='carrera',
            name='facultad',
            field=models.ForeignKey(related_name='carreras', blank=True, to='api.Facultad', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='grupo',
            unique_together=set([('codigo', 'facultad')]),
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together=set([('codigo', 'carrera', 'facultad')]),
        ),
        migrations.AlterUniqueTogether(
            name='carrera',
            unique_together=set([('codigo', 'facultad')]),
        ),
    ]

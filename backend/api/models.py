from django.db import models
from django.contrib.auth.models import User
# SIGNALS AND LISTENERS
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import smart_unicode


class Carrera(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    codigo = models.CharField(max_length=20, primary_key=True)
    plan = models.CharField(max_length=200, blank=True, null=True)
    facultad = models.ForeignKey('Facultad', related_name="carreras", blank=True, null=True)

    def __str__(self): 
        return self.nombre

class Facultad(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self): 
        return self.nombre

class Usuario(models.Model):  
    user = models.OneToOneField(User)  
    carrera = models.ForeignKey('Carrera', null=True, blank=True)
    cursos = models.ManyToManyField('Curso', through='UsuarioCurso')

    def __str__(self): 
        return self.user.username

class Curso(models.Model):
    APROBACION_CHOICES = (
        ('curso', 'Curso'),
        ('examen', 'Examen'),
    )
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=200)
    aprobacion = models.CharField(max_length=200, choices=APROBACION_CHOICES,null=True, blank=True)
    validez = models.IntegerField(null=True, blank=True)
    creditos = models.IntegerField(null=True, blank=True)
    previas_grupo = models.ManyToManyField('Grupo', blank=True)
    previas_curso = models.ManyToManyField('self', blank=True)
    antiprevias = models.ManyToManyField('self', blank=True)
    carrera = models.ForeignKey('Carrera', null=True, blank=True)

    class Meta: 
        unique_together = ("codigo", "carrera")

    def __unicode__(self): 
        return smart_unicode(self.codigo + " - " + self.nombre)


class Grupo(models.Model):
    nombre = models.CharField(max_length=128)
    puntaje_minimo = models.IntegerField()
    puntaje_maximo = models.IntegerField()
    cursos = models.ManyToManyField(Curso, through='GrupoCurso')

    def __str__(self):
        return self.nombre


class GrupoCurso(models.Model):
    puntaje_minimo = models.IntegerField()
    grupo = models.ForeignKey('Grupo')
    curso = models.ForeignKey('Curso')


class UsuarioCurso(models.Model):
    APROBACION_CHOICES = (
        ('curso_aprobado', 'Curso aprobado'),
        ('examen_aprobado', 'Examen Aprobado'),
    )
    tipo = models.CharField(max_length=200, choices=APROBACION_CHOICES)
    usuario = models.ForeignKey('Usuario')
    curso = models.ForeignKey('Curso')



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created: 
        profile, new = Usuario.objects.get_or_create(user=instance)



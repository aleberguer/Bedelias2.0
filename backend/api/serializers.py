from rest_framework import serializers
from .models import *

class CarreraSerializer(serializers.Serializer):
    class Meta:
    	model = Carrera
        fields = ('nombre')


class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Facultad

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Curso

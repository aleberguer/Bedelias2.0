from rest_framework import serializers
from .models import *

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Carrera
    	depth = 1

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Facultad

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Curso

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ("username", "first_name", "last_name", "email",)

class UsuarioSerializer(serializers.ModelSerializer):
	user = UserInfoSerializer()
	class Meta:
		model = Usuario
		depth = 1
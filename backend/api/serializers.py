from rest_framework import serializers
from .models import Carrera

class CarreraSerializer(serializers.Serializer):
    class Meta:
    	model = Carrera
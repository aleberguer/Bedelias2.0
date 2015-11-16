from rest_framework import viewsets, status, pagination
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.core import serializers

from .models import *
from .serializers import *


class CarreraViewSet(viewsets.ModelViewSet):
	queryset = Carrera.objects.all()
	serializer_class = CarreraSerializer


class FacultadViewSet(viewsets.ModelViewSet):
	queryset = Facultad.objects.all()
	serializer_class = FacultadSerializer

class CursoViewSet(viewsets.ModelViewSet):
	queryset = Curso.objects.all()[:1]
	serializer_class = CursoSerializer

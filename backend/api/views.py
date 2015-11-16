from rest_framework import viewsets, status, pagination
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

from .models import Carrera
from .serializers import CarreraSerializer


class CarreraViewSet(viewsets.ModelViewSet):
	queryset = Carrera.objects.all()
	serializer_class = CarreraSerializer
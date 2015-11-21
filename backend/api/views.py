from rest_framework import viewsets, status, pagination
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.core import serializers
from rest_framework import mixins
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

    @detail_route()
    def cursos(self, request, pk=None):
        cursos = Curso.objects.filter(carrera=self.get_object())

        page = self.paginate_queryset(cursos)
        if page is not None:
            serializer = CursoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(cursos, many=True)
        return Response(serializer.data)


class FacultadViewSet(viewsets.ModelViewSet):
    queryset = Facultad.objects.all()
    serializer_class = FacultadSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class UsuarioViewSet(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

'''
create user
'''
@csrf_exempt
def create_user(request):
    print request.body
    data = json.loads(request.body.decode("utf-8"))
    user = User()
    user.first_name = data["fullname"]
    user.username = data["username"]
    user.email = data["email"]
    user.password =make_password(data["password"])
    user.save()
    return HttpResponse(json.dumps(data), status=200)

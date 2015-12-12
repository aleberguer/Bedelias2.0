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

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    @detail_route()
    def cursos(self, request, pk=None):
        cursos = UsuarioCurso.objects.filter(usuario=self.get_object())

        page = self.paginate_queryset(cursos)
        if page is not None:
            serializer = UsuarioCursoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(cursos, many=True)
        return Response(serializer.data)

    @detail_route()
    def otros_cursos(self, request, pk=None):
        user = self.get_object()
        mis_cursos = UsuarioCurso.objects.filter(usuario=user)

        result = []
        for c in mis_cursos:
            result.append(c.id)

        cursos_carrera = Curso.objects.filter(carrera=user.carrera)
        cursos_carrera = cursos_carrera.exclude(id__in=result)

        # page = self.paginate_queryset(cursos_carrera)
        # if page is not None:
        #     serializer = CursoSerializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = CursoSerializer(cursos_carrera, many=True)
        return Response(serializer.data)

    @detail_route()
    def creditos(self, request, pk=None):
        cursos = UsuarioCurso.objects.filter(usuario=self.get_object())
        suma = 0
        for c in cursos:
            if (c.tipo == 'curso_aprobado' and c.curso.aprobacion == 'curso') or (c.tipo == 'examen_aprobado'):
                if c.curso.creditos is not None:
                    suma += c.curso.creditos

        return Response(suma)


    @detail_route(methods=['POST'])
    def agregar_curso(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        newLink = UsuarioCurso()

        newLink.usuario = Usuario.objects.get(id=pk)
        newLink.curso = Curso.objects.get(id=data['cursoId'])
        newLink.tipo = data['tipo']
        
        try:
            newLink.save()
            return HttpResponse("Curso ingresado con exito")
        except Exception, e:
            return HttpResponse(e)
    

    @detail_route(methods=['POST'])
    def borrar_curso(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        link = UsuarioCurso.objects.get(usuario__id=pk, curso__id=data['cursoId'] )

        try:
            link.delete()
            return HttpResponse("Curso borrado con exito")
        except Exception, e:
            return HttpResponse(e)
        

    @detail_route(methods=['POST'])
    def modificar_curso(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        link = UsuarioCurso.objects.get(usuario__id=pk, curso__id=data['cursoId'] )

        try:
            link.tipo = data['estado']
            link.save()
            return HttpResponse(json.dumps({ 'status':200, 'message': 'Curso modificado con exito'}))
        except Exception, e:
            return HttpResponse(e)


'''
create user
'''
@csrf_exempt
def create_user(request):
    print request.body
    data = json.loads(request.body.decode("utf-8"))
    if not User.objects.filter(username=data["username"]).exists():
        user = User()
        user.first_name = data["fullname"]
        user.username = data["username"]
        user.email = data["email"]
        user.password =make_password(data["password"])
        user.save()
        return HttpResponse(json.dumps(data), status=200)
    else:
        return HttpResponse("Ya existe un usuario con ese username", status=400)

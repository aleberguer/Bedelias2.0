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
from django.contrib.auth import authenticate, login
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

    @detail_route()
    def carreras(self, request, pk=None):
        print(str(self.get_object()))
        carreras = Carrera.objects.filter(facultad=self.get_object())

        print(str(carreras))
        serializer = CarreraSerializer(carreras, many=True)
        return Response(serializer.data)

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    def get_queryset(self):
        queryset = Curso.objects.all()
        query = self.request.query_params.get('q', None)
        if query is not None:
            queryset = queryset.filter(nombre__icontains=query, carrera__codigo='72-0')
        return queryset

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
    def posibles_cursos(self, request, pk=None):
        user = self.get_object()
        mis_cursos = UsuarioCurso.objects.filter(usuario=user)

        result = []
        for c in mis_cursos:
            result.append(c.curso.id)

        cursos_carrera = Curso.objects.filter(carrera=user.carrera)
        cursos_carrera = cursos_carrera.exclude(id__in=result)

        cursos_aprobados = []

        for c in mis_cursos:
            cursos_aprobados.append(c.curso.codigo)
        
        examenesa = UsuarioCurso.objects.filter(usuario=user, tipo="examen_aprobado")
        examenes_aprobados = []
        for c in examenesa:
            examenes_aprobados.append(c.curso.codigo)

        

        materiasACursar = []

        for curso in cursos_carrera:
            puedoCursar = True
            
            index = 0
            previas_tipoCurso = curso.previas_curso_tipoCurso.all()
            while puedoCursar and index < previas_tipoCurso.count():
                prev =  previas_tipoCurso[index]

                print (prev.aprobacion)

                if prev.aprobacion == 'curso' and (prev.codigo not in cursos_aprobados):
                    puedoCursar=False
                elif prev.aprobacion == 'examen' and (prev.codigo not in examenes_aprobados):
                    puedoCursar=False
                else:    
                    index += 1

            index = 0
            antiprevias_tipoCurso = curso.antiprevias_curso_tipoCurso.all()
            while puedoCursar and index < antiprevias_tipoCurso.count():
                prev =  antiprevias_tipoCurso[index]

                if prev.aprobacion == 'curso' and (prev.codigo in cursos_aprobados):
                    puedoCursar=False
                elif prev.aprobacion == 'examen' and (prev.codigo in examenes_aprobados):
                    puedoCursar=False
                else:    
                    index += 1

            index = 0
            previas_tipoGrupo = curso.previas_curso_tipoGrupo.all()
            while puedoCursar and index < previas_tipoGrupo.count():
                prev = previas_tipoGrupo[index]

                #########################################################
                puntaje = 0
                for materia_grupo in prev.cursos.all():

                    grcu = GrupoCurso.objects.filter(grupo=prev, curso=materia_grupo)
                    if grcu.exists():
                        for gc in grcu:
                            if gc.actividad == u'Curso aprobado' and (gc.curso.codigo in cursos_aprobados):
                                puntaje += gc.puntaje 
                            elif gc.actividad == u'Examen aprobado' and (gc.curso.codigo in examenes_aprobados):
                                puntaje += gc.puntaje 
                    
                #########################################################
               
                if  puntaje < prev.puntaje_minimo or puntaje > prev.puntaje_maximo:
                    puedoCursar = False
                else:
                    index +=1

            index = 0
            antiprevias_tipoGrupo = curso.antiprevias_curso_tipoGrupo.all()
            while puedoCursar and index < antiprevias_tipoGrupo.count():
                prev = antiprevias_tipoGrupo[index]

                #########################################################
                puntaje = 0
                for materia_grupo in prev.cursos.all():

                    grcu = GrupoCurso.objects.filter(grupo=prev, curso=materia_grupo)
                    if grcu.exists():
                        for gc in grcu:
                            if gc.actividad == u'Curso aprobado' and (gc.curso.codigo in cursos_aprobados):
                                puntaje += gc.puntaje 
                            elif gc.actividad == u'Examen aprobado' and (gc.curso.codigo in examenes_aprobados):
                                puntaje += gc.puntaje 
                #########################################################
               
                if  puntaje >= prev.puntaje_minimo and puntaje <= prev.puntaje_maximo:
                    puedoCursar = False
                else:
                    index +=1

            
            if puedoCursar:
                materiasACursar.append(curso)
                
        serializer = CursoSerializer(materiasACursar, many=True)
        return Response(serializer.data)

    @detail_route()
    def otros_cursos(self, request, pk=None):
        user = self.get_object()
        mis_cursos = UsuarioCurso.objects.filter(usuario=user)

        result = []
        for c in mis_cursos:
            result.append(c.curso.id)

        cursos_carrera = Curso.objects.filter(carrera=user.carrera)
        cursos_carrera = cursos_carrera.exclude(id__in=result)

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
            return HttpResponse(json.dumps({ "status": 200, "message": "Curso ingresado con exito" }))
        except Exception, e:
            return HttpResponse(e)

    @detail_route(methods=['POST'])
    def editar_curso(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        link = UsuarioCurso.objects.get(usuario__id=data['usuarioId'], curso__id=data['cursoId'] )

        link.tipo = data['tipo']

        try:
            link.save()
            return HttpResponse(json.dumps({ "status": 200, "message": "Curso modificado con exito" }))
        except Exception, e:
            return HttpResponse(e)


    @detail_route(methods=['POST'])
    def borrar_curso(self, request, pk=None):
        data = json.loads(request.body.decode("utf-8"))
        link = UsuarioCurso.objects.get(usuario__id=pk, curso__id=data['cursoId'] )

        try:
            link.delete()
            return HttpResponse(json.dumps({ "status": 200, "message": "Curso borrado con exito" }))
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
    data = json.loads(request.body.decode("utf-8"))
    if not User.objects.filter(username=data["username"]).exists():
        user = User()
        user.first_name = data["fullname"]
        user.username = data["username"]
        user.email = data["email"]
        user.password = make_password(data["password"])
        user.save()

        usuario = Usuario.objects.get(user=user)

        dataCarrera = data["carrera"]
        carrera = Carrera.objects.filter(codigo=dataCarrera["codigo"], facultad=dataCarrera["facultad"])[0]
        usuario.carrera = carrera
        usuario.save()

        serializer = UsuarioSerializer(usuario)

        return HttpResponse(json.dumps(serializer.data), status=200)
    else:
        return HttpResponse("Ya existe un usuario con ese username", status=400)

'''
login user
'''
@csrf_exempt
def login_user(request):
    data = json.loads(request.body.decode("utf-8"))
    user = authenticate(username=data["username"], password=data["password"])

    if user:
        if user.is_active:
            login(request, user)
            usuario = Usuario.objects.get(user=user)
            serializer = UsuarioSerializer(usuario)
            return HttpResponse(json.dumps(serializer.data), status=200)
        else:
            return HttpResponse("Your Rango account is disabled.")


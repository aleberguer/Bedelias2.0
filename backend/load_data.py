import json
from api.models import *
import os
from django.utils.encoding import smart_str, smart_unicode

cursos = Curso.objects.all()
for c in cursos:
	c.delete()

carrera = Carrera.objects.all()
for c in carrera:
	c.delete()

facultades = Facultad.objects.all()
for f in facultades:
	f.delete()

delete_grupos = Grupo.objects.all()
for d in delete_grupos:
	d.delete()

delete_grupos_curso = GrupoCurso.objects.all()
for d in delete_grupos_curso:
	d.delete()

baseName = "/Users/Alexander/Desktop/Procesados/Procesados/"

facultades = [d for d in os.listdir(baseName) if not(d.startswith('.'))]
for facultad in facultades:
	dirname = baseName
	facultad = facultad.encode('utf8')
	# Agrego Facutad.
	fac = Facultad()
	fac.nombre = facultad
	fac.save()

	dirname = os.path.join(dirname, facultad);
	carreras = [d for d in os.listdir(dirname) if not(d.startswith('.'))]

	for carr in carreras:
		carrera = Carrera()
		carrera.codigo = carr
		carrera.facultad = fac
		carrera.save()

		files = [f for f in os.listdir(os.path.join(dirname, carr)) if f.endswith('.json')]
		for filename in files:
			with open(os.path.join(dirname, carr, filename)) as json_file:
				json_data = json.load(json_file)
				curso = Curso()
				curso.nombre = json_data['NombreMateria'].encode('utf8')
				curso.codigo = json_data['CodigoMateria'].strip().encode('utf8')
				curso.facultad = fac
				carrera.nombre = json_data['Carrera'].encode('utf8')

				try: 
					with open(os.path.join(dirname, carr, "CreditosMaterias", filename)) as creditos_file:
						creditos_data = json.load(creditos_file)
						curso.nombre = creditos_data['Nombre'].encode('utf8')
						curso.codigo = creditos_data['Codigo'].strip().encode('utf8')
						if creditos_data['TipoAprobacion'].encode('utf8')  == "Examen ":
							curso.aprobacion = 'examen'
						else:
							curso.aprobacion = 'curso'
						curso.validez = creditos_data['MesesValidez'].encode('utf8')
						curso.creditos = creditos_data['Creditos'].encode('utf8')
				except Exception as e:
					v = ''
					# print "la materia no tiene creditos"
					# print e

				curso.carrera = carrera
				curso.save()

		if not carrera.nombre:		
			carrera.delete()
		else:
			carrera.save()
			for filename in files:
				with open(os.path.join(dirname, carr, filename)) as previas_file:
					json_data = json.load(previas_file)

					codigo = json_data['CodigoMateria'].encode('utf8')
					curso = Curso.objects.filter(codigo=codigo, carrera=carrera, facultad=fac)

					'''
					 *
					 * ANTIPREVIAS 
					 *
					'''

					'''
					  Antiprevias de curso
					'''
					antiprevias_curso = json_data['Curso*']
					
					for key, antiprevia in antiprevias_curso.iteritems():
						if "MateriasGrupo" in antiprevia:
							grupo_actual = Grupo.objects.filter(codigo=antiprevia['CodigoGrupo'], facultad=fac)
							
							if (not grupo_actual.exists()):
								gru = Grupo()
								gru.codigo = antiprevia['CodigoGrupo']
								gru.facultad = fac
								gru.puntaje_minimo = antiprevia['PuntajeMinimo']
								gru.puntaje_maximo = antiprevia['PuntajeMaximo']
								gru.nombre = antiprevia['NombreGrupo']
								gru.save()

								for idx, materia in antiprevia['MateriasGrupo'].iteritems():
									codigo_materia = materia["Materia"]
									curso2 = Curso.objects.filter(codigo=codigo_materia, carrera=carrera, facultad=fac)
									if curso2.exists():
										grupo_curso = GrupoCurso()
										grupo_curso.curso = curso2[0]
										grupo_curso.grupo = gru
										grupo_curso.puntaje =  materia["Puntaje"]
										grupo_curso.actividad =  materia["Actividad"]
										grupo_curso.save()

							curso[0].antiprevias_curso_tipoGrupo.add(grupo_actual[0])
							curso[0].save()
						else:
							curso_actual = Curso.objects.filter(
								codigo=antiprevia['CodigoMateria'], 
								carrera=carrera, 
								facultad=fac
							)
							if curso_actual.exists():
								curso[0].antiprevias_curso_tipoCurso.add(curso_actual[0])
								curso[0].save()

					'''
					  Antiprevias de examen
					'''
					antiprevias_examen = json_data['Examen*']
					
					for key, antiprevia in antiprevias_examen.iteritems():
						if "MateriasGrupo" in antiprevia:
							grupo_actual = Grupo.objects.filter(codigo=antiprevia['CodigoGrupo'], facultad=fac)
							
							if (not grupo_actual.exists()):
								gru = Grupo()
								gru.codigo = antiprevia['CodigoGrupo']
								gru.facultad = fac
								gru.puntaje_minimo = antiprevia['PuntajeMinimo']
								gru.puntaje_maximo = antiprevia['PuntajeMaximo']
								gru.nombre = antiprevia['NombreGrupo']
								gru.save()

								for idx, materia in antiprevia['MateriasGrupo'].iteritems():
									codigo_materia = materia["Materia"]
									curso2 = Curso.objects.filter(codigo=codigo_materia, carrera=carrera, facultad=fac)
									if curso2.exists():
										grupo_curso = GrupoCurso()
										grupo_curso.curso = curso2[0]
										grupo_curso.grupo = gru
										grupo_curso.puntaje =  materia["Puntaje"]
										grupo_curso.actividad =  materia["Actividad"]
										grupo_curso.save()

							curso[0].antiprevias_examen_tipoGrupo.add(grupo_actual[0])
							curso[0].save()
						else:
							curso_actual = Curso.objects.filter(
								codigo=antiprevia['CodigoMateria'], 
								carrera=carrera, 
								facultad=fac
							)
							if curso_actual.exists():
								curso[0].antiprevias_examen_tipoCurso.add(curso_actual[0])
								curso[0].save()

					# ***********************************************************
					# ***********************************************************
					# ***********************************************************

					'''
					 *
					 * PREVIAS 
					 *
					'''

					'''
					  Previas de curso
					'''
					previas_curso = json_data['Curso']

					for key, previa in previas_curso.iteritems():
						if "MateriasGrupo" in previa:
							grupo_actual = Grupo.objects.filter(codigo=previa['CodigoGrupo'], facultad=fac)
							
							if (not grupo_actual.exists()):
								gru = Grupo()
								gru.codigo = previa['CodigoGrupo']
								gru.facultad = fac
								gru.puntaje_minimo = previa['PuntajeMinimo']
								gru.puntaje_maximo = previa['PuntajeMaximo']
								gru.nombre = previa['NombreGrupo']
								gru.save()

								for idx, materia in previa['MateriasGrupo'].iteritems():
									codigo_materia = materia["Materia"]
									curso2 = Curso.objects.filter(codigo=codigo_materia, carrera=carrera, facultad=fac)
									if curso2.exists():
										grupo_curso = GrupoCurso()
										grupo_curso.curso = curso2[0]
										grupo_curso.grupo = gru
										grupo_curso.puntaje =  materia["Puntaje"]
										grupo_curso.actividad =  materia["Actividad"]
										grupo_curso.save()

							curso[0].previas_curso_tipoGrupo.add(grupo_actual[0])
							curso[0].save()
						else:
							curso_actual = Curso.objects.filter(
								codigo=previa['CodigoMateria'], 
								carrera=carrera, 
								facultad=fac
							)
							if curso_actual.exists():
								curso[0].previas_curso_tipoCurso.add(curso_actual[0])
								curso[0].save()

					'''
					  Previas de examen
					'''
					previas_examen = json_data['Examen']
					
					for key, previa in previas_examen.iteritems():
						if "MateriasGrupo" in previa:
							grupo_actual = Grupo.objects.filter(codigo=previa['CodigoGrupo'], facultad=fac)
							
							if (not grupo_actual.exists()):
								gru = Grupo()
								gru.codigo = previa['CodigoGrupo']
								gru.facultad = fac
								gru.puntaje_minimo = previa['PuntajeMinimo']
								gru.puntaje_maximo = previa['PuntajeMaximo']
								gru.nombre = previa['NombreGrupo']
								gru.save()

								for idx, materia in previa['MateriasGrupo'].iteritems():
									codigo_materia = materia["Materia"]
									curso2 = Curso.objects.filter(codigo=codigo_materia, carrera=carrera, facultad=fac)
									if curso2.exists():
										grupo_curso = GrupoCurso()
										grupo_curso.curso = curso2[0]
										grupo_curso.grupo = gru
										grupo_curso.puntaje =  materia["Puntaje"]
										grupo_curso.actividad =  materia["Actividad"]
										grupo_curso.save()

							curso[0].previas_examen_tipoGrupo.add(grupo_actual[0])
							curso[0].save()
						else:
							curso_actual = Curso.objects.filter(
								codigo=previa['CodigoMateria'], 
								carrera=carrera, 
								facultad=fac
							)
							if curso_actual.exists():
								curso[0].previas_examen_tipoCurso.add(curso_actual[0])
								curso[0].save()
	


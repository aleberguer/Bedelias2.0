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

carreras_invalidas = []

dirname = "/Users/Alexander/Desktop/Procesados/Procesados/INGENIERIA/"

dirs = [d for d in os.listdir(dirname) if not(d.startswith('.'))]

for di in dirs:
	if (di != '20-51' and di != '20-9' and di != '20-93' and di != '20-95' and di != '22-3'
		and di != '27-3'):
		carrera = Carrera()
		carrera.codigo = di
		carrera.save()

		files = [f for f in os.listdir(dirname + di) if f.endswith('.json')]
		for filename in files:
			with open(dirname + di + "/" + filename) as json_file:
				json_data = json.load(json_file)
				# curso = Curso()
				# curso.nombre = json_data['NombreMateria'].encode('utf8')
				# curso.codigo = json_data['CodigoMateria'].encode('utf8')
				# curso.save()
				carrera.nombre = json_data['Carrera'].encode('utf8') 

		if not carrera.nombre:		
			carrera.delete()
		else:
			carrera.save()
			files = [f for f in os.listdir(dirname + di + "/CreditosMaterias/") if f.endswith('.json')]
			for filename in files:
				if (filename != 'Grupo .json' and filename != 'Materia .json' and filename != 'Grupo.json' and filename != 'Materia.json'):
					with open(dirname + di + "/CreditosMaterias/" + filename) as json_file:
						json_data = json.load(json_file)
						curso = Curso()
						curso.nombre = json_data['Nombre'].encode('utf8')
						curso.codigo = json_data['Codigo'].encode('utf8')
						if json_data['TipoAprobacion'].encode('utf8')  == "Examen ":
							curso.aprobacion = 'examen'
						else:
							curso.aprobacion = 'curso'
						curso.validez = json_data['MesesValidez'].encode('utf8')
						curso.creditos = json_data['Creditos'].encode('utf8')
						curso.carrera = carrera
						curso.save()

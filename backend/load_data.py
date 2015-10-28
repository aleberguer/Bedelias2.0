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

dirname = "/Users/Alexander/Desktop/Procesados/Procesados/INGENIERIA/"

dirs = [d for d in os.listdir(dirname) if not(d.startswith('.'))]

for di in dirs:

	carrera = Carrera()
	carrera.codigo = di
	carrera.save()

	files = [f for f in os.listdir(dirname + di) if f.endswith('.json')]
	for filename in files:
		with open(dirname + di + "/" + filename) as json_file:
			json_data = json.load(json_file)
			curso = Curso()
			curso.nombre = json_data['NombreMateria'].encode('utf8')
			curso.codigo = json_data['CodigoMateria'].encode('utf8')
			curso.save()
			carrera.nombre = json_data['Carrera'].encode('utf8') 
	carrera.save()


from django.contrib import admin
from .models import Carrera, Usuario, Curso, Grupo, GrupoCurso, UsuarioCurso

admin.site.register(Carrera)
admin.site.register(Curso)


class GrupoCursoInline(admin.TabularInline):
    model = GrupoCurso
    extra = 1

class GrupoAdmin(admin.ModelAdmin):
    inlines = (GrupoCursoInline,)

admin.site.register(Grupo, GrupoAdmin)

class UsuarioCursoInline(admin.TabularInline):
    model = UsuarioCurso
    extra = 1

class UsuarioAdmin(admin.ModelAdmin):
    inlines = (UsuarioCursoInline,)

admin.site.register(Usuario, UsuarioAdmin)
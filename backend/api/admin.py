from django.contrib import admin
from .models import Carrera, Usuario, Curso, Grupo, GrupoCurso, UsuarioCurso, Facultad

admin.site.register(Carrera)

admin.site.register(Facultad)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'carrera', 'facultad')
    list_display_links = ('codigo', 'nombre','carrera','facultad' )
    list_per_page = 25

admin.site.register(Curso, CursoAdmin)

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
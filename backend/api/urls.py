from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'carreras', CarreraViewSet, base_name='carreras')
router.register(r'facultades', FacultadViewSet, base_name='facultades')
router.register(r'cursos', CursoViewSet, base_name='cursos')
router.register(r'usuario', UsuarioViewSet, base_name='usuario')

urlpatterns = router.urls
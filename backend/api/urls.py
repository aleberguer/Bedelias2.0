from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'carreras', CarreraViewSet, base_name='carreras')
router.register(r'facultades', FacultadViewSet, base_name='facultades')
router.register(r'cursos', CursoViewSet, base_name='cursos')

urlpatterns = router.urls
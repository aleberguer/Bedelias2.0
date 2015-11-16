from .views import CarreraViewSet 
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'carreras', CarreraViewSet, base_name='carreras')

urlpatterns = router.urls
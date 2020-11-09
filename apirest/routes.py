from rest_framework import routers

from core.views import ClienteViewSet

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

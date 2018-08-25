from rest_framework import routers
#from tutorial.quickstart import views
from .viewset import ProveedorViewSet,CompradetalleViewset

router = routers.DefaultRouter()
router.register('proveedores', ProveedorViewSet)
router.register('compradetalle', CompradetalleViewset)

#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
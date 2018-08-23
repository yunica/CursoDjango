
from django.urls import path
from .views import listaproductos,detalleproductos
urlpatterns = [
    path('listaproductos', listaproductos),
 path('listaproductos/<int:pk>', detalleproductos),
 #   path('listarusuario', primeravista),
  #  path('listarusuario2', primeravista),
                 # path('admin/', admin.site.urls),
              ] 
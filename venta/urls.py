
from django.urls import path
from .views import listaproductos,detalleproductos,agregarproveedor, agregarproveedor2
app_name = "app1" 
urlpatterns = [
    path('listaproductos', listaproductos, name="lista"),
 path('listaproductos/<int:pk>', detalleproductos, name="detalle"),
 path('agregarproveedor', agregarproveedor, name="agregarp"),
 path('agregarproveedor2', agregarproveedor2, name="agregarp2"),

 #   path('listarusuario', primeravista),
  #  path('listarusuario2', primeravista),
                 # path('admin/', admin.site.urls),
              ] 
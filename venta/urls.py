
from django.urls import path
from .views import listaproductos,detalleproductos,agregarproveedor
app_name = "app1" 
urlpatterns = [
    path('listaproductos', listaproductos, name="lista"),
 path('listaproductos/<int:pk>', detalleproductos, name="detalle"),
 path('agregarproveedor', agregarproveedor, name="agregarp"),

 #   path('listarusuario', primeravista),
  #  path('listarusuario2', primeravista),
                 # path('admin/', admin.site.urls),
              ] 

from django.urls import path
from .views import primeravista
urlpatterns = [

    path('listarusuario', primeravista),
                 # path('admin/', admin.site.urls),
              ] 
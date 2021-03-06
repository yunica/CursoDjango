from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', include('publico.urls', namespace="publico")),
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('venta/', include('venta.urls', namespace="app1")),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

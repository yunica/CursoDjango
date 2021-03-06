from django.urls import path, include
from .views import listaproductos, detalleproductos, MyPDF, some_view, DemoPDFView, render_pdf_view, agregarproveedor, \
    agregarproveedor2, buscarproducto, ListarProveedor, ProveedorCreate
from venta.apis import urls as apiurls

app_name = "app1"
urlpatterns = [
    path('listaproductos', listaproductos, name="lista"),
    path('listaproductos/<int:pk>', detalleproductos, name="detalle"),
    path('agregarproveedor', agregarproveedor, name="agregarp"),
    path('agregarproveedor2', agregarproveedor2, name="agregarp2"),
    path('buscarproduto', buscarproducto, name="buscarp"),
    path('listarp', ListarProveedor.as_view(), name="listarp"),
    path('new', ProveedorCreate.as_view(), name="listarp"),
    path('imprimir/<int:pk>/informe', some_view, name="imprimir"),

    path('api/', include(apiurls.router.urls)),

    #   path('listarusuario', primeravista),
    #  path('listarusuario2', primeravista),
    # path('admin/', admin.site.urls),
]

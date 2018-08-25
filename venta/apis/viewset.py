from rest_framework import viewsets
from venta.models import Proveedor, CompraDetalle
from .serializer import ProveedorSerializer,CompraDetalleSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.filter(estado=False)
    serializer_class = ProveedorSerializer


class CompradetalleViewset(viewsets.ModelViewSet):
    queryset = CompraDetalle.objects.filter(estado=True)
    serializer_class = CompraDetalleSerializer

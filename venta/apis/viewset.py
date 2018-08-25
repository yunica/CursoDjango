from rest_framework import viewsets
from venta.models import Proveedor
from .serializer import ProveedorSerializer


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.filter(estado=False)
    serializer_class = ProveedorSerializer

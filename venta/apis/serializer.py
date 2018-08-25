from rest_framework import serializers
from venta.models import Proveedor,CompraDetalle


class ProveedorSerializer(serializers.ModelSerializer):
   # codigo = serializers.CharField
    class Meta:
        model = Proveedor
        fields = ('nombre','id')

class CompraDetalleSerializer(serializers.ModelSerializer):
   # codigo = serializers.CharField
    class Meta:
        model = CompraDetalle
        fields = '__all__'
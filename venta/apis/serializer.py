from rest_framework import serializers
from venta.models import Proveedor


class ProveedorSerializer(serializers.ModelSerializer):
   # codigo = serializers.CharField
    class Meta:
        model = Proveedor
        fields = ('nombre','id')

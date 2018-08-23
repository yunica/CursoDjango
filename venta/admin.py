from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Compra)
admin.site.register(CompraDetalle)
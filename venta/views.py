from django.shortcuts import render
from .models import Producto
# Create your views here.

def listaproductos(request):
    oproducto = Producto.objects.filter(estado=True)
    contenido ={
        "lista":oproducto,
        "valor": 654654654654
    }
    return render(request,'venta/listaproductos.html',contenido)


def detalleproductos(request, pk=None):

    if pk:
        contenido ={
            "producto" : Producto.objects.get(pk=pk)
        }
        return render(request,'venta/detailproducto.html',contenido)


from django.shortcuts import render, HttpResponseRedirect
from .models import Producto
from .formularios import segundoformulario
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def listaproductos(request):
    oproducto = Producto.objects.filter(estado=True)
    contenido = {
        "lista": oproducto,
        "valor": 654654654654
    }
    print(request.user)
    return render(request, 'venta/listaproductos.html', contenido)


def detalleproductos(request, pk=None):

    if pk:
        contenido = {
            "producto": Producto.objects.get(pk=pk)
        }
        return render(request, 'venta/detailproducto.html', contenido)


def agregarproveedor(request):
    contenido = {
        "form" :segundoformulario
    }
    if request.method == 'POST':
        formulario = segundoformulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            #return HttpResponseRedirect('/venta/listaproductos')
    return render(request, 'venta/crearproveedor.html', contenido)

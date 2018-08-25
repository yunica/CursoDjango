from django.shortcuts import render, HttpResponseRedirect
from .models import Producto, Proveedor
from .formularios import segundoformulario
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView



# Create your views here.

#@login_required(login_url='/login')
def listaproductos(request):
    oproducto = Producto.objects.filter(estado=True)
    contenido = {
        "lista": oproducto,
        "valor": 654654654654
    }

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


def agregarproveedor2(request):
    if request.method == 'POST':
        oproveedor = Proveedor(
            nombre = str(request.POST.get('nombre')).upper(),
            descripcion =str(request.POST.get('descripcion')),
            estado = False
        )

        
        oproveedor.save()

    return render(request, 'venta/agregarproveedor2.html')

def buscarproducto(request):
    if request.method == 'GET':
        oproducto = Producto.objects.filter(nombre__contains=request.GET.get('nombreproductos'))
        contenido={
            "lista":oproducto
            }
        return render(request, 'venta/listaproductos.html', contenido)


class ListarProveedor(ListView):
    model = Proveedor
    template_name ='venta/listarproasview.html'
    context_object_name = 'lista_proveedores'
    queryset = Proveedor.objects.filter(estado = True)


class ProveedorCreate(CreateView):
    model = Proveedor
    template_name = 'venta/crearprovee.html'
    success_url = '/venta/listarp'
    fields = '__all__'
    
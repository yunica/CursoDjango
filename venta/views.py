from django.shortcuts import render, HttpResponseRedirect
from .models import Producto, Proveedor
from .formularios import segundoformulario
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView
#  print
import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa


def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL  # Typically /static/
    sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL  # Typically /static/media/
    mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


def render_pdf_view(request):
    template_path = 'print/test.html'
    context = {'datos': range(0, 200)}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisaStatus = pisa.CreatePDF(html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Create your views here.

# @login_required(login_url='/login')
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
        "form": segundoformulario
    }
    if request.method == 'POST':
        formulario = segundoformulario(request.POST)
        if formulario.is_valid():
            formulario.save()
            # return HttpResponseRedirect('/venta/listaproductos')
    return render(request, 'venta/crearproveedor.html', contenido)


def agregarproveedor2(request):
    if request.method == 'POST':
        oproveedor = Proveedor(
            nombre=str(request.POST.get('nombre')).upper(),
            descripcion=str(request.POST.get('descripcion')),
            estado=False
        )

        oproveedor.save()

    return render(request, 'venta/agregarproveedor2.html')


def buscarproducto(request):
    if request.method == 'GET':
        oproducto = Producto.objects.filter(nombre__contains=request.GET.get('nombreproductos'))
        contenido = {
            "lista": oproducto
        }
        return render(request, 'venta/listaproductos.html', contenido)


class ListarProveedor(ListView):
    model = Proveedor
    template_name = 'venta/listarproasview.html'
    context_object_name = 'lista_proveedores'
    queryset = Proveedor.objects.filter(estado=True)


class ProveedorCreate(CreateView):
    model = Proveedor
    template_name = 'venta/crearprovee.html'
    success_url = '/venta/listarp'
    fields = '__all__'


# imprimir v2   https://github.com/nigma/django-easy-pdf

from easy_pdf.views import PDFTemplateView
from django.utils.timezone import now


class DemoPDFView(PDFTemplateView):
    template_name = 'print/easy_pdf.html'
    pdf_filename = 'hello.pdf'

    def get_context_data(self, **kwargs):
        return super(DemoPDFView, self).get_context_data(
            pagesize='A4',
            title='Hi there!',
            today=now(),
            **kwargs
        )

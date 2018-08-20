from django.shortcuts import render

# Create your views here.
def primeravista(request):
    return render(request,'usuario/listarusuario.html')
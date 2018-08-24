from django.shortcuts import render,redirect ,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def loginview(request):
    if request.user.is_authenticated:
        return redirect('/venta/listaproductos')
    elif request.method == 'POST':
        variable1 = str(request.POST.get('campo1'))
        variable2 = str(request.POST.get('campo2'))
        user = authenticate(request, username=variable1, password=variable2)
        if user is not None:
            login(request, user)
            return redirect('/venta/listaproductos')
    return render (request, 'publico/login.html')

def logoutview(request):
    logout(request)

    return redirect('/')

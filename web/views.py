from django.shortcuts import render

# Create your views here.
def lista_producto(request):
    return render(request, 'web/lista_producto.html', {})

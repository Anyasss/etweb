from django.shortcuts import render
from web.models import Producto
from django.utils import timezone

def lista_producto(request):
    producto = Producto.objects.all()
    return render(request, 'web/lista_producto.html', {'producto': producto})

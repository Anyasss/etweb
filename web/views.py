from django.shortcuts import render
from web.models import Producto
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm

def lista_producto(request):
    producto = Producto.objects.all()
    return render(request, 'web/lista_producto.html', {'producto': producto})

def detalle_producto(request, pk):
    producto = Producto.objects.get(Producto, pk=pk)
    return render(request, 'web/detalle_producto.html', {'producto': producto})

def nuevo_producto(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.author = request.user
            producto.created_date = timezone.now()
            producto.save()
            return redirect('web.views.detalle_producto', pk=producto.pk)
    else:
        form = PostForm()
    return render(request, 'web/nuevo_producto.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Producto
# Create your views here.

def verProductos(request):
    """Renderizado de Productos"""
    producto = Producto.objects.all()
    return render(request,"productos.html",{"productos":producto})

def detalleProducto(request, prod_id):
    #Buscar el producto por id
    producto = get_object_or_404(Producto , id = prod_id)
    return render(request,'ver_producto.html',{'producto':producto})
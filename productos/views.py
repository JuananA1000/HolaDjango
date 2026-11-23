from django.shortcuts import render # render() nos permite combinar HTML con datos Python y RENDERIZARLOS en el navegador.
from .models import Product

def lista_productos(request):
    productos = Product.objects.all() # esto equivale a un SELECT * FROM productos_product; en sql
    contexto = {'productos': productos} # este diccionario permite enviar información desde Python a una plantilla HTML
    return render(request, 'productos/lista.html', contexto) # Renderizamos la plantilla HTML

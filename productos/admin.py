from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # OJO A ESTO: se añadirá una coma al final de cada campo, si no, se interprera como una cadena de texto entre paréntesis, no una tupla.
    list_display = ('id', 'nombre', 'precio', 'stock', 'fecha_creacion',) # Indica qué columnas queremos visualizar en el listado de productos.
    search_fields = ('nombre',)  # Añade un buscador que permitirá localizar productos por su nombre.
    list_filter = ('fecha_creacion',)  # Añade filtros laterales para filtrar los productos según su fecha de creación.
    ordering = ('nombre',)  # Ordena los productos alfabéticamente por su nombre.

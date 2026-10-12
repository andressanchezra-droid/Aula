
from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "id_producto",
        "nombre",
        "precio",
        "cantidad_stock",
        "activo",
        "fecha_actualizacion",
    )

    list_filter = ("activo",)
    search_fields = ("nombre", "descripcion")

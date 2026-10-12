
from django.urls import path
from . import api

urlpatterns = [
    path(
        "api/productos/",
        api.productos_collection,
        name="api_productos"
    ),
    path(
        "api/productos/<int:pk>/",
        api.producto_detalle,
        name="api_producto_detalle"
    ),
]

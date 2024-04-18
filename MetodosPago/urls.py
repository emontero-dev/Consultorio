from django.urls import path
from . import views


urlpatterns = [
    path("facturacion/", views.facturacion_list, name='lista_facturas'),
    path("facturacion_details/<int:id>/", views.facturacion_details, name='facturacion_details'),
    path("insertar_factura/", views.crear_factura, name='insertar_factura'),
]

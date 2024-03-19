from django.urls import path
from . import views


urlpatterns = [
    path("facturacion/", views.facturacion_list, name='lista_facturas'),
]

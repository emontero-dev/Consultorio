from django.contrib import admin
from . import models

@admin.register(models.MetodosPago)
class MetodosPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'MetodosPagoNombre', 'MetodosPagoActivo')
    list_display_links = ('id', 'MetodosPagoNombre')


@admin.register(models.Pagos)
class PagosAdmin(admin.ModelAdmin):
    list_display = ('id', 'PagosNombre', 'Pagos_PacienteId', 'PagosFechaPago', 'Pagos_Monto', 'PagosActivo')
    list_display_links = ('id', 'PagosNombre')

@admin.register(models.Facturas)
class FacturasAdmin(admin.ModelAdmin):
    list_display = ('id', 'Facturas_PacienteId', 'FacturasFechaFactura', 'Facturas_Monto', "FacturasDetalle")
    list_display_links = ('id', 'Facturas_PacienteId')
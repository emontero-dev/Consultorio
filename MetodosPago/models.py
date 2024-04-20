from django.db import models
from Pacientes.models import Pacientes

class MetodosPago(models.Model):
    MetodosPagoNombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Metodo de Pago")
    MetodosPagoActivo = models.BooleanField(default=True)

    def __str__(self):
        return self.MetodosPagoNombre

    class Meta:
        verbose_name_plural = "Metodos de Pago"

class Pagos(models.Model):
    PagosNombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Detalle")
    Pagos_PacienteId = models.ForeignKey(Pacientes, on_delete=models.DO_NOTHING, null=False, blank=False, verbose_name="Paciente")
    PagosFechaPago = models.DateField(null=False, blank=False, verbose_name="Fecha de Pago")
    Pagos_Monto = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2, verbose_name="Monto")
    PagosActivo = models.BooleanField(default=True)

    def __str__(self):
        return self.PagosNombre

    class Meta:
        verbose_name_plural = "Pagos"

class Facturas(models.Model):
    Facturas_PacienteId = models.ForeignKey(Pacientes, on_delete=models.DO_NOTHING, null=False, blank=False)
    FacturasFechaFactura = models.DateField(null=False, blank=False)
    Facturas_Monto = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    FacturasDetalle = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.FacturasFechaFactura

    class Meta:
        verbose_name_plural = "Facturas"
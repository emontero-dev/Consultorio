from django.shortcuts import render
from . import models

def facturacion_list(request):
    Pagos = models.Pagos.objects.all()
    total = 0
    for pago in Pagos:
        total =+ pago.Pagos_Monto

    return render(request, 'facturacion.html', {'Pagos': Pagos, 'total': total})

# Create your views here.

from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
from django.core.paginator import Paginator


def facturacion_list(request):
    pagos_queryset = models.Pagos.objects.all()

    paginator = Paginator(pagos_queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    total = sum(pago.Pagos_Monto for pago in pagos_queryset)

    context = {
        'page_obj': page_obj,
        'total': total
    }

    return render(request, 'facturacion.html', context)

def facturacion_details(request, id):
    Pagos = models.Pagos.objects.get(id=id)
    facturaid = f'FA-000{Pagos.id}'
    return render(request, 'facturacion_details.html', {'Pagos': Pagos , 'facturaid': facturaid})

def crear_factura(request):
    if request.method == 'POST':
        FacturasFechaFactura = request.POST.get('FacturasFechaFactura')
        Facturas_Monto = request.POST.get('Facturas_Monto')
        Facturas_PagoId = request.POST.get('Facturas_PagoId')
        FacturasNombre = request.POST.get('FacturasNombre')
        Facturas_PacienteId = request.POST.get('Facturas_PacienteId')

        try:
            paciente = models.Pacientes.objects.get(id=Facturas_PacienteId)
        except models.Pacientes.DoesNotExist:
            messages.error(request, 'El paciente no existe.')
            return redirect('insertar_factura')

        if request.method == 'POST':
            nuevo_factura = models.Facturas(
                FacturasNombre = FacturasNombre,
                Facturas_PacienteId = paciente,
                FacturasFechaFactura = FacturasFechaFactura,
                Facturas_Monto = Facturas_Monto,
                FacturasActivo = True
            )
            nuevo_factura.save()
            messages.success(request, 'Se ha guardado la Factura exitosamente.')
            return redirect('lista_facturas')

    pacientes = models.Pacientes.objects.all()

    context = {
        'pacientes': pacientes,
    }

    return render(request, 'insertar_factura.html', context)

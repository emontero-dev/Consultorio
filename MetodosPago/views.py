from django.shortcuts import render,redirect
from . import models
from django.contrib import messages

def facturacion_list(request):
    Pagos = models.Pagos.objects.all()
    total = 0
    for pago in Pagos:
        total =+ pago.Pagos_Monto

    return render(request, 'facturacion.html', {'Pagos': Pagos, 'total': total})

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

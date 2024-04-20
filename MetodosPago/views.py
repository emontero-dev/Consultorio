from django.shortcuts import render,redirect
from . import models
from django.contrib import messages
from django.core.paginator import Paginator
from .form import PagosForm


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
        form = PagosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_facturas')
    else:
        form = PagosForm()
    return render(request, 'insertar_factura.html', {'form': form})

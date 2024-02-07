from django.shortcuts import render
from .models import Pacientes

def pacient_edit(request,pk):

    paciente = Pacientes.objects.get(id=pk)
    return render(request, 'pacientes_edit.html',{'paciente':paciente} )

def patient_information(request,pk):
    paciente = Pacientes.objects.get(id=pk)
    return render(request, 'information.html',{'paciente':paciente} )

def pacientes(request):
    context = {
        'pacientes': Pacientes.objects.all()
    }
    return render(request, 'pacientes.html', context)


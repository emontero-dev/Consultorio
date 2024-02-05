from django.shortcuts import render
from .models import Pacientes

def pacientes(request):
    context = {
        'pacientes': Pacientes.objects.all()
    }
    return render(request, 'pacientes.html', context)

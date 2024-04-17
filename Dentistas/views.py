
from django.shortcuts import render, redirect
from django.contrib import messages
from Pacientes.models import Dentistas

def insertar_dentista(request):
    print("Insertar dentista vista llamada")
    if request.method == 'POST':
        DentistasNombre = request.POST.get('DentistasNombre')
        DentistasApellido = request.POST.get('DentistasApellido')
        DentistasEspecialidad = request.POST.get('DentistasEspecialidad')
        DentistasTelefono = request.POST.get('DentistasTelefono')
        DentistasEmail = request.POST.get('DentistasEmail')
        DentistasEmailNormalizado = request.POST.get('DentistasEmailNormalizado')

        if DentistasNombre and DentistasApellido and DentistasEspecialidad and DentistasTelefono and DentistasEmail and DentistasEmailNormalizado:
            nuevo_dentista = Dentistas(
                DentistasNombre=DentistasNombre,
                DentistasApellido=DentistasApellido,
                DentistasEspecialidad=DentistasEspecialidad,
                DentistasTelefono=DentistasTelefono,
                DentistasEmail=DentistasEmail,
                DentistasEmailNormalizado=DentistasEmailNormalizado,

            )
            nuevo_dentista.save()
            messages.success(request, 'Se ha guardado el dentista exitosamente.')
            return redirect('Lista_Dentistas')  # Asegúrate de definir esta vista
        else:
            messages.error(request, 'Por favor, complete todos los campos.')

    return render(request, 'insertar_dentista.html')


def listar_dentistas(request):
    dentistas = Dentistas.objects.all()
    return render(request, 'lista_dentistas.html', {'dentistas': dentistas})


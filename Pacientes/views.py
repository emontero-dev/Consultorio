from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pacientes, Dentistas, Tratamientos


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
            return redirect('listar_dentistas')  # Asegúrate de definir esta vista
        else:
            messages.error(request, 'Por favor, complete todos los campos.')

    return render(request, 'insertar_dentista.html')



def listar_dentistas(request):
    dentistas = Dentistas.objects.all()
    return render(request, 'lista_dentistas.html', {'dentistas': dentistas})

def insertar_paciente(request):
    print("Insertar paciente vista llamada")
    if request.method == 'POST':
        PacientesNombre = request.POST.get('PacientesNombre')
        PacientesApellido = request.POST.get('PacientesApellido')
        PacientesDireccion = request.POST.get('PacientesDireccion')
        PacientesTelefono = request.POST.get('PacientesTelefono')
        PacientesEmail = request.POST.get('PacientesEmail')
        PacientesEmailNormalizado = request.POST.get('PacientesEmailNormalizado')
        PacientesActivo = request.POST.get('PacientesActivo') == 'on'  

        # Mejorar la validación de campos
        if PacientesNombre and PacientesApellido and PacientesDireccion and PacientesTelefono and PacientesEmail and PacientesEmailNormalizado:
            nuevo_paciente = Pacientes(
                PacientesNombre=PacientesNombre,
                PacientesApellido=PacientesApellido,
                PacientesDireccion=PacientesDireccion,
                PacientesTelefono=PacientesTelefono,
                PacientesEmail=PacientesEmail,
                PacientesEmailNormalizado=PacientesEmailNormalizado,
                PacientesActivo=PacientesActivo,
            )
            nuevo_paciente.save()
            messages.success(request, 'Se ha guardado el paciente exitosamente.')
            return redirect('listar_pacientes') 
        else:
            messages.error(request, 'Por favor, complete todos los campos.')

    return render(request, 'insertar_paciente.html')

def listar_pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})

def insertar_tratamiento(request):
    print("Insertar tratamiento vista llamada")
    if request.method == 'POST':
        nombre_tratamiento = request.POST.get('nombre_tratamiento')
        precio = request.POST.get('Precio')

        # Mejorar la validación de campos
        if nombre_tratamiento and precio:
            nuevo_tratamiento = Tratamientos(
                nombre_tratamiento=nombre_tratamiento,
                Precio=precio,
            )
            nuevo_tratamiento.save()
            messages.success(request, 'Se ha guardado el tratamiento exitosamente.')
            return redirect('listar_tratamientos') 
        else:
            messages.error(request, 'Por favor, complete todos los campos.')

    return render(request, 'insertar_tratamiento.html')


def listar_tratamientos(request):
    tratamientos = Tratamientos.objects.all()
    return render(request, 'lista_tratamientos.html', {'tratamientos': tratamientos})
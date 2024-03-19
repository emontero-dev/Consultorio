from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pacientes, Dentistas, Tratamientos, TratamientoPaciente,Historial
from django.core.exceptions import ValidationError


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
        precio_str = request.POST.get('precio')

        try:
            precio = float(precio_str)  # Intenta convertir el precio a un número decimal
        except ValueError:
            messages.error(request, 'El precio debe ser un número válido.')
            return render(request, 'insertar_tratamiento.html')

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



def insertar_historial(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente_id')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

       
        nuevo_historial = Historial(
            Paciente_id_foreign_key_id=paciente_id,
            Description=description,
            StartDate=start_date,
            EndDate=end_date
        )
        nuevo_historial.save()
        messages.success(request, 'Historial guardado correctamente.')
        return redirect('insertar_historial')  

    return render(request, 'insertar_historial.html')

def listar_historiales(request):
    historiales = Historial.objects.all()
    return render(request, 'listar_historiales.html', {'historiales': historiales})


def agregar_tratamiento_paciente(request):
    if request.method == 'POST':
        tratamiento_id = request.POST.get('tratamiento')
        pieza_dental = request.POST.get('pieza_dental')
        paciente_id = request.POST.get('paciente')

        if tratamiento_id and pieza_dental and paciente_id:
            try:
                tratamiento = Tratamientos.objects.get(pk=tratamiento_id)
                paciente = Pacientes.objects.get(pk=paciente_id)
            except (Tratamientos.DoesNotExist, Pacientes.DoesNotExist):
                # Manejar si el tratamiento o el paciente no existen
                messages.error(request, 'El tratamiento o el paciente no existen.')
                return redirect('agregar_tratamiento_paciente')

            tratamiento_paciente = TratamientoPaciente(
                Tratamiento_id_foreignkey=tratamiento,
                Pieza_dental=pieza_dental,
                foreign_paciente=paciente
            )
            tratamiento_paciente.save()
            messages.success(request, 'El tratamiento ha sido agregado al paciente correctamente.')
            return redirect('agregar_tratamiento_paciente')
        else:
           
            messages.error(request, 'Por favor, complete todos los campos.')
            return redirect('agregar_tratamiento_paciente')

    tratamientos = Tratamientos.objects.all()
    pacientes = Pacientes.objects.all()
    return render(request, 'agregar_tratamiento_paciente.html', {'tratamientos': tratamientos, 'pacientes': pacientes})

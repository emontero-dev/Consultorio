from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pacientes,  Tratamientos, TratamientoPaciente,ImagenesMedicasTipos,  ImagenesMedicas, Dentistas, Agenda
from django.core.exceptions import ValidationError
from .forms import PacienteForm, DentistaForm, DentistaInformationForm, AgendaForm
from django.core.paginator import Paginator

def eliminar_paciente(request, paciente_id):
    paciente = Pacientes.objects.get(id=paciente_id)
    paciente.delete()
    return redirect('Pacientes')

def dentista_delete(request, pk):
    dentista = Dentistas.objects.get(pk=pk)
    if request.method == "POST":
        dentista.delete()
        return redirect('Lista_Dentistas')  # Redirige a la página de lista de dentistas después de la eliminación
    return render(request, 'confirm_delete_dentista.html', {'dentista': dentista})


def dentista_information(request, dentista_id):
    dentista = Dentistas.objects.get(pk=dentista_id)
    form = DentistaInformationForm(instance=dentista)
    return render(request, 'information_dentist.html', {'form': form})

def dentista_edit(request, pk):
    dentista = Dentistas.objects.get(pk=pk)
    if request.method == "POST":
        form = DentistaForm(request.POST, instance=dentista)
        if form.is_valid():
            form.save()
            return redirect('edit_dentista', pk=pk)  # Redirige a la página de detalles del dentista
    else:
        form = DentistaForm(instance=dentista)
    return render(request, 'edit_dentist.html', {'form': form})

def pacient_edit(request, pk):
    paciente = Pacientes.objects.get(pk=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha actualizado el paciente exitosamente.')
            return redirect('edit', pk=pk)  # Redirige a la misma página de edición
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'edit_paciente.html', {'form': form})

def patient_information(request, pk):
    paciente = Pacientes.objects.get(id=pk)

    imagenes_medicas = ImagenesMedicas.objects.filter(ImagenesMedicas_PacienteId=paciente)

    tratamientos = TratamientoPaciente.objects.filter(foreign_paciente=paciente)
    
    return render(request, 'information.html', {'paciente': paciente, 'imagenes_medicas': imagenes_medicas, 'tratamientos': tratamientos})

def pacientes(request):

    pacientes = Pacientes.objects.filter(PacientesActivo=True)

    paginator = Paginator(pacientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj
    }

    return render(request, 'pacientes.html', context)

def pacientes_inactivos(request):

    pacientes = Pacientes.objects.filter(PacientesActivo=False)

    paginator = Paginator(pacientes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'pacientes_inactivos.html', context)


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
            return redirect('Pacientes')
        else:
            messages.error(request, 'Por favor, complete todos los campos.')

    return render(request, 'insertar_paciente.html')



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


def insertar_imagen_medica(request):
    pacientes = Pacientes.objects.all()  # Obtener todos los pacientes
    tipos_imagenes = ImagenesMedicasTipos.objects.all()  # Obtener todos los tipos de imágenes
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        tipo_id = request.POST.get('tipo_imagen')  # Cambié el nombre del campo
        descripcion = request.POST.get('descripcion')
        imagen = request.FILES.get('imagen')

        if paciente_id and tipo_id and descripcion and imagen:
            paciente = Pacientes.objects.get(pk=paciente_id)
            tipo_imagen = ImagenesMedicasTipos.objects.get(id=tipo_id)
            
            nueva_imagen_medica = ImagenesMedicas(
                ImagenesMedicas_PacienteId=paciente,
                ImagenesMedicas_Tipos=tipo_imagen,
                ImagenesMedicasTiposDescripcion=descripcion,
                ImagenesMedicas_Img=imagen
            )
            nueva_imagen_medica.save()
            messages.success(request, 'Se ha guardado la imagen médica exitosamente.')
            return redirect('insertar_imagen_medica')
        else:
            messages.error(request, 'Por favor, complete todos los campos.')

    return render(request, 'insertar_imagen_medica.html', {'pacientes': pacientes, 'tipos_imagenes': tipos_imagenes})

def ver_imagenes_medicas(request):
    imagenes_medicas = ImagenesMedicas.objects.all()
    return render(request, 'ver_imagenes_medicas.html', {'imagenes_medicas': imagenes_medicas})

def insertar_tipo_imagen_medica(request):
    if request.method == 'POST':
        tipo_nombre = request.POST.get('tipo_nombre')
        tipo_activo = request.POST.get('tipo_activo') == 'on'

        
        if tipo_nombre:
            nuevo_tipo_imagen = ImagenesMedicasTipos(
                ImagenesMedicasTiposNombre=tipo_nombre,
                ImagenesMedicasTiposActivo=tipo_activo
            )
            nuevo_tipo_imagen.save()
            messages.success(request, 'Se ha guardado el tipo de imagen médica exitosamente.')
            return redirect('insertar_tipo_imagen_medica')
        else:
            messages.error(request, 'Por favor, ingrese un nombre para el tipo de imagen médica.')

    return render(request, 'insertar_tipo_imagen_medica.html')

def ver_imagenes_tipos(request):
    tipos_imagenes = ImagenesMedicasTipos.objects.all()
    return render(request, 'ver_imagenes_tipos.html', {'tipos_imagenes': tipos_imagenes})


def agenda_create(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Paciente agendado correctamente.')
            return redirect('agenda_list')
    else:
        form = AgendaForm()
    return render(request, 'agenda.html', {'form': form})

def AgendaList(request):
    agendas = Agenda.objects.all().filter(Confirmada=False)

    paginator = Paginator(agendas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'agendas': page_obj,
    }

    return render(request, 'agenda_list.html', context)

def AgendaListFinalizado(request):
    agendas = Agenda.objects.all().filter(Confirmada=True)

    paginator = Paginator(agendas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'agendas': page_obj,
    }

    return render(request, 'agenda_list_finalizado.html', context)

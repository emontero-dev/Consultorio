from django.db import models    

class Dentistas(models.Model):
    """ VARIABLES DEL DENTISTA """
    DentistasID = models.AutoField(primary_key=True)
    DentistasNombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    DentistasApellido = models.CharField(max_length=100, null=False, blank=False, verbose_name="Apellidos")
    DentistasEspecialidad = models.CharField(max_length=100, null=False, blank=False, verbose_name="Especialidad")
    DentistasTelefono = models.CharField(max_length=10, null=False, blank=False, verbose_name="Teléfono")
    DentistasEmail = models.CharField(max_length=100, null=False, blank=False, verbose_name="Email")
    DentistasEmailNormalizado = models.CharField(max_length=100, null=False, blank=False, verbose_name="Email Normalizado")
   
    def __str__(self):
        return self.DentistasNombre + " " + self.DentistasApellido

    class Meta:
        verbose_name_plural = "Dentistas"


class Pacientes(models.Model):
    
    id = models.AutoField(primary_key=True)
    PacientesNombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    PacientesApellido = models.CharField(max_length=100, null=False, blank=False, verbose_name="Apellidos")
    PacientesDireccion = models.CharField(max_length=100, null=False, blank=False, verbose_name="Dirección")
    PacientesTelefono = models.CharField(max_length=10, null=False, blank=False, verbose_name="Teléfono")
    PacientesEmail = models.CharField(max_length=100, null=False, blank=False, verbose_name="Email")
    PacientesEmailNormalizado = models.CharField(max_length=100, null=False, blank=False, verbose_name="Email Normalizado")
    PacientesActivo = models.BooleanField(default=True, verbose_name="Activo")

    def __str__(self):
        return self.PacientesNombre + " " + self.PacientesApellido

    class Meta:
        verbose_name_plural = "Pacientes"

class Tratamientos(models.Model):
    Tratamientos_ID = models.AutoField(primary_key=True)
    nombre_tratamiento = models.CharField(max_length=100, null=False, blank=False, default='valor_predeterminado', verbose_name="nombre_tratamiento")
    Precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_tratamiento

class TratamientoPaciente(models.Model):
    Tratamiento_Paciente_id = models.AutoField(primary_key=True)
    Tratamiento_id_foreignkey = models.ForeignKey(Tratamientos, on_delete=models.CASCADE)
    Pieza_dental = models.IntegerField()
    foreign_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)



class Historial(models.Model):
    Id_Historial = models.AutoField(primary_key=True)
    Paciente_id_foreign_key = models.ForeignKey('Pacientes', on_delete=models.CASCADE, default=1)
    Description = models.TextField()
    StartDate = models.DateField()
    EndDate = models.DateField()

class ImagenesMedicasTipos(models.Model):
    """ TIPOS DE IMAGENES PARA REALIZAR DROPDOWN """
    tiposImagenes = ["Rayos X", "Scanner", "Tomograficas", "Resonancia Magnetica"]

    """ VARIABLES QUE SE SE EJECUTAN EN EL MODELO """
    ImagenesMedicasTiposNombre = models.CharField(max_length=100, null=False, blank=False, choices=[(x, x) for x in tiposImagenes])
    ImagenesMedicasTiposActivo = models.BooleanField(default=True)

    def __str__(self):
        return self.ImagenesMedicasTiposNombre

    class Meta:
        verbose_name_plural = "Imagenes Medicas Tipos"

class ImagenesMedicas(models.Model):
    """TABLA DE IMAGENES MEDICAS PARA NORMALIZAR """
    ImagenesMedicas_PacienteId = models.ForeignKey(Pacientes, on_delete=models.DO_NOTHING, null=False, blank=False)
    ImagenesMedicas_Tipos = models.ForeignKey(ImagenesMedicasTipos, on_delete=models.DO_NOTHING, null=False, blank=False)
    ImagenesMedicasTiposDescripcion = models.CharField(max_length=200, null=False, blank=False)
    ImagenesMedicas_Img = models.ImageField(upload_to="ImagenesMedicas", null=False, blank=False)

    def __str__(self):
        return self.ImagenesMedicas_Tipos

    class Meta:
        verbose_name_plural = "Imagenes Medicas"


class Agenda(models.Model):
    id = models.AutoField(primary_key=True )
    Dentistas_id = models.ForeignKey(Dentistas, on_delete=models.DO_NOTHING, verbose_name="Seleccione el Dentista")
    Pacientes_id = models.ForeignKey(Pacientes, on_delete=models.DO_NOTHING , verbose_name="Seleccione el Paciente")
    Fecha = models.DateTimeField(verbose_name="Fecha y Hora", null=False, blank=False)
    Status = models.BooleanField(default=True, verbose_name="Activo")
    Confirmada = models.BooleanField(default=False, verbose_name="Finalizado")
    TipoTratamiento = models.ForeignKey(Tratamientos, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f"Agenda para {self.Pacientes_id.PacientesNombre} {self.Pacientes_id.PacientesApellido}"

    class Meta:
        verbose_name_plural = "Agenda"
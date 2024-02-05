from django.db import models

class Pacientes(models.Model):
    """ VARIABLES DEL PACIENTE """
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

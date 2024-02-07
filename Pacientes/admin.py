from django.contrib import admin
from . import models

# PANEL ADMINISTRATIVO MODIFICADO

admin.site.site_header = "Panel Administrativo - Odonto Tech "
admin.site.site_title = "Consultorio Medico"
admin.site.index_title = "Odonto Tech "



@admin.register(models.Pacientes)
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'PacientesNombre', 'PacientesApellido', 'PacientesEmail', 'PacientesEmailNormalizado', 'PacientesActivo')
    list_display_links = ('id', 'PacientesNombre')


@admin.register(models.ImagenesMedicasTipos)
class Admin(admin.ModelAdmin):
    list_display = ('id', 'ImagenesMedicasTiposNombre', 'ImagenesMedicasTiposActivo')
    list_display_links = ('id', 'ImagenesMedicasTiposNombre')


@admin.register(models.ImagenesMedicas)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'ImagenesMedicas_PacienteId', 'ImagenesMedicas_Tipos', 'ImagenesMedicasTiposDescripcion', 'ImagenesMedicas_Img')
    list_display_links = ('id', 'ImagenesMedicas_PacienteId')

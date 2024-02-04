from django.db import models

class Dentista(models.Model):
    dentista_id = models.IntegerField(primary_key=True, verbose_name="id_dentista", unique=True)
    nombre = models.CharField(max_length=255, verbose_name="nombre", blank=False)
    apellido1 = models.CharField(max_length=255, verbose_name="apellido1", blank=False)
    apellido2 = models.CharField(max_length=255, verbose_name="apellido2", blank=False)
    especialidad = models.CharField(max_length=255, verbose_name="especialidad", blank=False)
    numero_telefono = models.IntegerField(verbose_name="numero_telefono", null=True, blank=False)
    e_mail = models.CharField(max_length=255, verbose_name="e_mail", null=True, blank=False)
    e_mail_normalizado = models.CharField(max_length=255, verbose_name="e_mail_normalizado", null=True, blank=False)

class Paciente(models.Model):
    paciente_id = models.IntegerField(primary_key=True, verbose_name="id_paciente", unique=True)
    nombre = models.CharField(max_length=255, verbose_name="nombre", blank=False)
    apellido1 = models.CharField(max_length=255, verbose_name="apellido1", blank=False)
    apellido2 = models.CharField(max_length=255, verbose_name="apellido2", blank=False)
    fecha_nacimiento = models.DateField(verbose_name="Fecha", blank=False)
    direccion = models.CharField(max_length=255, verbose_name="direccion", blank=False)
    numero_telefono = models.IntegerField(verbose_name="numero_telefono", null=True, blank=False)
    e_mail = models.CharField(max_length=255, verbose_name="e_mail", null=True, blank=False)
    e_mail_normalizado = models.CharField(max_length=255, verbose_name="e_mail_normalizado", null=True, blank=False)

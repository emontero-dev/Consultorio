from django.db import models

class Dentista(models.Model):
    dentista_id= models.IntegerField(primary_key=True, verbose_name="id_dentista", unique=True)
    nombre=models.CharField(max_lenght=255, verbose_name="nombre", blank=False)
    apellido1=models.CharField(max_lenght=255, verbose_name="apellido1", blank=False)
    apellido2=models.CharField(max_lenght=255, verbose_name="apellido2", blank=False)
    especialidad=models.CharField(max_lenght=255, verbose_name="especialidad", blank=False)
    

class Paciente(models.Model):
    paciente_id= models.IntegerField(primary_key=True, verbose_name="id_paciente", unique=True)
    nombre=models.CharField(max_lenght=255, verbose_name="nombre", blank=False)
    apellido1=models.CharField(max_lenght=255, verbose_name="apellido1", blank=False)
    apellido2=models.CharField(max_lenght=255, verbose_name="apellido2", blank=False)
    fecha_nacimiento= models.DateField(verbose_name="Fecha", blank=False)
    direccion= models.CharField(max_lenght=255, verbose_name="apellido2", blank=False)
    numero_telefono= cliente_edad = models.IntegerField(verbose_name="Edad Cliente", blank=False)
    e_mail=models.CharField(max_lenght=255, verbose_name="especialidad", blank=False)


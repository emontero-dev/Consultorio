# Generated by Django 5.0 on 2024-02-18 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pacientes', '0002_alter_imagenesmedicastipos_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dentistas',
            fields=[
                ('DentistasID', models.AutoField(primary_key=True, serialize=False)),
                ('DentistasNombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('DentistasApellido', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('DentistasEspecialidad', models.CharField(max_length=100, verbose_name='Especialidad')),
                ('DentistasTelefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('DentistasEmail', models.CharField(max_length=100, verbose_name='Email')),
                ('DentistasEmailNormalizado', models.CharField(max_length=100, verbose_name='Email Normalizado')),
                ('DentistasActivo', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name_plural': 'Dentistas',
            },
        ),
        migrations.CreateModel(
            name='Tratamientos',
            fields=[
                ('Tratamientos_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='PacientesActivo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='PacientesApellido',
            field=models.CharField(max_length=100, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='PacientesDireccion',
            field=models.CharField(max_length=100, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='PacientesEmail',
            field=models.CharField(max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='PacientesEmailNormalizado',
            field=models.CharField(max_length=100, verbose_name='Email Normalizado'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='PacientesNombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='PacientesTelefono',
            field=models.CharField(max_length=10, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='TratamientoPaciente',
            fields=[
                ('Tratamiento_Paciente_id', models.AutoField(primary_key=True, serialize=False)),
                ('Pieza_dental', models.IntegerField()),
                ('foreign_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.pacientes')),
                ('Tratamiento_id_foreignkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.tratamientos')),
            ],
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('Id_Historial', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.TextField()),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Paciente_id_foreign_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.pacientes')),
                ('dentista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.dentistas')),
                ('Tratamiento_Paciente_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pacientes.tratamientopaciente')),
            ],
        ),
    ]
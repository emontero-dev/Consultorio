# Generated by Django 5.0 on 2024-02-21 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pacientes', '0004_remove_dentistas_dentistasactivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tratamientos',
            name='nombre_tratamiento',
            field=models.CharField(default='valor_predeterminado', max_length=100, verbose_name='nombre_tratamiento'),
        ),
    ]
# Generated by Django 5.0 on 2024-03-19 00:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pacientes', '0006_remove_historial_paciente_id_foreign_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historial',
            name='Paciente_id_foreign_key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Pacientes.pacientes'),
        ),
    ]

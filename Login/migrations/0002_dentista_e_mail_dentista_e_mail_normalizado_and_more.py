# Generated by Django 5.0 on 2024-02-04 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dentista',
            name='e_mail',
            field=models.CharField(max_length=255, null=True, verbose_name='e_mail'),
        ),
        migrations.AddField(
            model_name='dentista',
            name='e_mail_normalizado',
            field=models.CharField(max_length=255, null=True, verbose_name='e_mail_normalizado'),
        ),
        migrations.AddField(
            model_name='dentista',
            name='numero_telefono',
            field=models.IntegerField(default=0, verbose_name='numero_telefono'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='e_mail_normalizado',
            field=models.CharField(max_length=255, null=True, verbose_name='e_mail_normalizado'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='e_mail',
            field=models.CharField(max_length=255, null=True, verbose_name='e_mail'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero_telefono',
            field=models.IntegerField(default=0, verbose_name='numero_telefono'),
        ),
    ]

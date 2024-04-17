# forms.py

from django import forms
from .models import Pacientes, Dentistas

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['PacientesNombre', 'PacientesApellido', 'PacientesDireccion', 'PacientesTelefono', 'PacientesEmail', 'PacientesActivo']


class DentistaForm(forms.ModelForm):
    class Meta:
        model = Dentistas
        fields = ['DentistasNombre', 'DentistasApellido', 'DentistasEspecialidad', 'DentistasTelefono', 'DentistasEmail']

class DentistaInformationForm(forms.ModelForm):
    class Meta:
        model = Dentistas
        fields = '__all__'  # Esto incluirá todos los campos del modelo Dentistas en el formulario
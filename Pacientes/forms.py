# forms.py

from django import forms
from .models import Pacientes, Dentistas

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['PacientesNombre', 'PacientesApellido', 'PacientesDireccion', 'PacientesTelefono', 'PacientesEmail', 'PacientesActivo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


class DentistaForm(forms.ModelForm):
    class Meta:
        model = Dentistas
        fields = ['DentistasNombre', 'DentistasApellido', 'DentistasEspecialidad', 'DentistasTelefono', 'DentistasEmail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})

class DentistaInformationForm(forms.ModelForm):
    class Meta:
        model = Dentistas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})
# forms.py

from django import forms
from .models import Pacientes, Dentistas, Agenda

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = ['PacientesNombre', 'PacientesApellido', 'PacientesDireccion', 'PacientesTelefono', 'PacientesEmail',
                  'PacientesActivo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['PacientesNombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['PacientesApellido'].widget.attrs.update({'class': 'form-control'})
        self.fields['PacientesDireccion'].widget.attrs.update({'class': 'form-control'})
        self.fields['PacientesTelefono'].widget.attrs.update({'class': 'form-control'})
        self.fields['PacientesEmail'].widget.attrs.update({'class': 'form-control'})
        self.fields['PacientesActivo'].widget.attrs.update({'class': 'form-check-input ' + 'm-2'})


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

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['Pacientes_id', 'Dentistas_id', 'Fecha', 'Status', 'Confirmada',  'TipoTratamiento']
        widgets = {
            'Pacientes_id': forms.Select(attrs={'class': 'form-control' + ' ' + 'mb-2'}),
            'Dentistas_id': forms.Select(attrs={'class': 'form-control' + ' ' + 'mb-2'}),
            'Fecha': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'Status': forms.CheckboxInput(attrs={'class': 'form-check-input' + ' ' + 'mb-2' + ' ' + 'ml-2'}),
            'Confirmada': forms.CheckboxInput(attrs={'class': 'form-check-input' + ' ' + 'mb-2' + ' ' + 'ml-2' }),
            'TipoTratamiento': forms.Select(attrs={'class': 'form-control' + ' ' + 'mb-2' }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

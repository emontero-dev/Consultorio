from django import forms
from .models import MetodosPago, Pagos, Facturas

class PagosForm(forms.ModelForm):
    PagosActivo = forms.BooleanField(initial=True, widget=forms.HiddenInput())
    class Meta:
        model = Pagos
        fields = ['PagosNombre', 'Pagos_PacienteId', 'PagosFechaPago', 'Pagos_Monto', 'PagosActivo']
        widgets = {
            'PagosNombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Pagos_PacienteId': forms.Select(attrs={'class': 'form-control'}),
            'PagosFechaPago': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'Pagos_Monto': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
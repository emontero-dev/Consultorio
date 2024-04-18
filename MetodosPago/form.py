from django import forms
from .models import MetodosPago, Pagos, Facturas

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = '__all__'

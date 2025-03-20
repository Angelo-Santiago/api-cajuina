from django import forms
from .models import Table

class MesaForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'name', 'capacity', 'status']

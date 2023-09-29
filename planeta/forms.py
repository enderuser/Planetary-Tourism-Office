from django import forms
from .models import Planeta, Distancia

class PlanetaForm(forms.ModelForm):
    class Meta:
        model = Planeta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class DistanciaForm(forms.ModelForm):
    class Meta:
        model = Distancia
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
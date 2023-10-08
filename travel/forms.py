from django import forms
from .models import Planet, DistanciaEntrePlanetas, Travel

class PlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class DistanciaForm(forms.ModelForm):
    class Meta:
        model = DistanciaEntrePlanetas
        fields = '__all__'

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['departure', 'arriving', 'data', 'time']

        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class PesquisaViagemForm(forms.Form):
    departure = forms.ModelChoiceField(queryset=Planet.objects.all(), label='Planeta de Origem')
    arriving = forms.ModelChoiceField(queryset=Planet.objects.all(), label='Planeta de Destino')
    data = forms.DateField(label='Data da Viagem')
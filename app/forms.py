from django.forms import ModelForm, TextInput, DateInput

from app.models import Aniversarios


class AniversariosForm(ModelForm):
    class Meta:
        model = Aniversarios
        fields = ('aniversariante', 'dt_aniversario')
        widgets = {
            'aniversariante': TextInput(attrs={'class': 'form-control'}),
            'dt_aniversario': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

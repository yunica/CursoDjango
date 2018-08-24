from django import forms
from .models import Proveedor


class primerformulario(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your website', required=False)
    comentario = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ingresa un comentario'}))


class segundoformulario(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
                'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingresa un nombre'}),
                'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'ingresa una descripcion'}),
            
            }

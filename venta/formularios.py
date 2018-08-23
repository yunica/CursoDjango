from django import forms

class primerformulario(forms.Form):
    name = forms.CharField(label='Your name')
    url = forms.URLField(label='Your website', required=False)
    comentario = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'ingresa un comentario'}))
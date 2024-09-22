from django import forms

class RegistroFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    documento = forms.IntegerField()
    email = forms.EmailField()








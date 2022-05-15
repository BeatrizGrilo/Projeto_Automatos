from django import forms
from django.forms import ModelForm
from .models import Automato, MaquinaTuring



class AutomatoForm(ModelForm):
    class Meta:
        model = Automato
        fields = '__all__'

        widgets = {
            'descricao' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'alfabeto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'estados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'estadoinicial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'estadodeaceitacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'transicoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
        }

class ValidarForm(forms.Form):
    expressao = forms.CharField()

class MaquinaTuringForm(ModelForm):
    class Meta:
        model = MaquinaTuring
        fields = '__all__'

        widgets = {
            'descricao' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'estados': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'estadoinicial': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'estadodeaceitacao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
            'transicoes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição...'}),
        }

class ValidarTMForm(forms.Form):
    expressao = forms.CharField()
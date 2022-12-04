from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TareaForm(forms.ModelForm):

    PRIORITIES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
    prioridad = forms.ChoiceField(choices=PRIORITIES)

    class Meta:
        model = Tarea
        fields = ['tarea', 'fecha_entrega', 'prioridad']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'}),
            'prioridad': forms.Select(attrs={'class': 'form-select'})
        }


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'password1', 'password2']
        help_texts = {k: '' for k in fields}
        labels = {'first_name': 'Nombre/s',
                  'last_name': 'Apellido/s', 'username': 'Nombre de usuario',
                  'password1': 'Contraseña', 'password2': 'Confirmar contraseña'}
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class binarySearchForm(forms.ModelForm):
    class Meta:
        model = bsElement
        fields = ['id_number']
        labels = {'id_number': 'Numero de tarea a buscar'}
        widgets = {
            'id_number': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'min': '1'})
        }

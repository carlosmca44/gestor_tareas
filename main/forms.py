from django import forms
from .models import Tarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = ['tarea', 'fecha_entrega']
        widgets = {
            'fecha_entrega': forms.DateInput(attrs={'type': 'date'})
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

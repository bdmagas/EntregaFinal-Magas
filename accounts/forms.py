from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import ClearableFileInput
from .models import Perfil

class CustomClearableFileInput(ClearableFileInput):
    initial_text = 'Actual'
    input_text = 'MODIFICAR'
    clear_checkbox_label = 'ELIMINAR'
    
class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'contact-form'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'contact-form'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'contact-form'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'contact-form'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'contact-form'}))
    password2 = forms.CharField(label='Repita Contraseña', widget=forms.PasswordInput(attrs={'class':'contact-form'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'contact-form'}),
            'last_name': forms.TextInput(attrs={'class': 'contact-form'}),
            'email': forms.EmailInput(attrs={'class': 'contact-form'}),
        }

class EditarProfileExtendidoForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'contact-form', 'type': 'date'}, format='%Y-%m-%d'),
            'avatar': CustomClearableFileInput(attrs={'class': 'contact-form'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Esta parte asegura que, si ya hay fecha_nacimiento, se muestre bien en el input
        if self.instance and self.instance.fecha_nacimiento:
            self.initial['fecha_nacimiento'] = self.instance.fecha_nacimiento.strftime('%Y-%m-%d')
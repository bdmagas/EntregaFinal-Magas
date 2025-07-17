from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Valoracion, VideoJuego, Plataforma

class CustomClearableFileInput(ClearableFileInput):
    initial_text = 'Actualmente'
    input_text = 'MODIFICAR'
    clear_checkbox_label = 'ELIMINAR'
    
class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['user_name', 'juego', 'estrellas', 'comentarios']
        widgets = {
            'estrellas': forms.HiddenInput(),
            'user_name': forms.TextInput(attrs={'class': 'contact-form', 'readonly': 'readonly'}),
            'juego': forms.Select(attrs={'class': 'contact-form'}),
            'comentarios': forms.Textarea(attrs={'class': 'contact-form', 'rows': 4}),
        }

class VideoJuegoForm(forms.ModelForm):
    class Meta:
        model = VideoJuego
        fields = ['nombre', 'genero', 'tag', 'plataformas', 'lanzamiento', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'contact-form'}),
            'genero': forms.TextInput(attrs={'class': 'contact-form'}),
            'tag': forms.TextInput(attrs={'class': 'contact-form'}),
            'plataformas': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '6'}),
            'lanzamiento': forms.DateInput(attrs={'class': 'contact-form', 'type': 'date'}, format='%Y-%m-%d'),
            'imagen': CustomClearableFileInput(attrs={'class': 'contact-form'}),     
        }

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'contact-form'}),
            'descripcion': forms.TextInput(attrs={'class': 'contact-form'}),
        }
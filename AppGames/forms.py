from django import forms
from .models import Valoracion, VideoJuego, Plataforma

class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['user_name', 'juego', 'estrellas', 'comentarios']
        widgets = {
            'estrellas': forms.HiddenInput(),
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'juego': forms.Select(attrs={'class': 'form-control'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class VideoJuegoForm(forms.ModelForm):
    class Meta:
        model = VideoJuego
        fields = ['nombre', 'genero', 'tag', 'plataformas', 'lanzamiento', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'plataformas': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'lanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
        }
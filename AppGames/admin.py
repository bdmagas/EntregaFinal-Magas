from django.contrib import admin
from .models import VideoJuego, Plataforma

# Register your models here.
@admin.register(VideoJuego)
class VideoJuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'genero', 'mostrar_plataformas', 'lanzamiento', 'tag')

    def mostrar_plataformas(self, obj):
        return ", ".join([p.nombre for p in obj.plataformas.all()])

    mostrar_plataformas.short_description = 'Plataformas'

@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ('nombre','descripcion')
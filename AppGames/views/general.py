from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from ..models import VideoJuego, Favorito

# Create your views here.
def inicio(request):
    return render(request, "AppGames/index.html")

def about(request):
    return render(request, "AppGames/about_me.html")


@login_required
def toggle_favorito(request, juego_id):
    juego = VideoJuego.objects.get(id=juego_id)
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, juego=juego)

    if not created:
        favorito.delete()
        return JsonResponse({'favorito': False})
    return JsonResponse({'favorito': True})
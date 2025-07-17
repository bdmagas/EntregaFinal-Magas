from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import get_resolver, URLPattern, URLResolver
from ..models import VideoJuego, Favorito

# Create your views here.
def inicio(request):
    return render(request, "AppGames/index.html")

def about(request):
    return render(request, "AppGames/about_me.html")

APP_PREFIXES = ['games', 'reviews', 'platforms', 'about', 'sitemap']

def get_named_urls(urlpatterns, prefix=''):
    urls = []
    for entry in urlpatterns:
        if isinstance(entry, URLPattern):
            if entry.name and any(entry.name.startswith(p) for p in APP_PREFIXES) and (not entry.name.startswith('admin')):
                urls.append({
                    'name': entry.name,
                    'url': prefix + str(entry.pattern)
                })
        elif isinstance(entry, URLResolver):
            nested_prefix = prefix + str(entry.pattern)
            urls += get_named_urls(entry.url_patterns, prefix=nested_prefix)
    return urls

@login_required
def sitemap(request):
    resolver = get_resolver()
    urls = get_named_urls(resolver.url_patterns)
    return render(request, 'AppGames/sitemap.html', {'urls': urls})


@login_required
def toggle_favorito(request, juego_id):
    juego = VideoJuego.objects.get(id=juego_id)
    favorito, created = Favorito.objects.get_or_create(usuario=request.user, juego=juego)

    if not created:
        favorito.delete()
        return JsonResponse({'favorito': False})
    return JsonResponse({'favorito': True})
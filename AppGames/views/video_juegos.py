from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import VideoJuego
from ..forms import VideoJuegoForm
import string

def ver_videojuegos(request):
    """
    Se muestran todos los juegos disponibles con varias opciones de selección:
        - Letra inicial
        - Genero
        - Tags
        - SEARCH: Query
    """   
    juegos = VideoJuego.objects.all().order_by('nombre')

    letra = request.GET.get('letra')
    tag = request.GET.get('tag')
    genero = request.GET.get('genero')
    page_number = request.GET.get('page')
    query = request.GET.get('q', '')

    if query:
        juegos = juegos.filter(Q(nombre__icontains=query)).order_by('nombre')   # buscar/search
    else:
        if letra:
            juegos = juegos.filter(nombre__istartswith=letra).order_by('nombre')  # filtrar por inicial
        if tag:
            juegos = juegos.filter(tag__iexact=tag).order_by('nombre')  # filtrar por tag
        if genero:
            juegos = juegos.filter(genero__iexact=genero).order_by('nombre')    # filtrar por genero
    
    letras = list(string.ascii_uppercase)  # ['A', 'B', 'C', ...]
    tags = VideoJuego.objects.values_list('tag', flat=True).distinct()
    generos = VideoJuego.objects.values_list('genero', flat=True).distinct()

    paginator = Paginator(juegos, 15)  # 15 por página
    page_obj = paginator.get_page(page_number)

    # retorna los videojuegos encontrados
    contexto = {
        "juegos": juegos,
        "letras": letras,
        "letra_seleccionada": letra,
        "tags": tags,
        "tag_seleccionado": tag,
        "generos": generos,
        "genero_seleccionado": genero,    
        "query": query,
        "page_obj": page_obj,
    }

    return render(request, "AppGames/video_juegos.html", contexto)

def nuevo_videojuego(request):
    """
    Agregar un nuevo juego mediante un form, de acuerdo con el modelo VideoJuego
    input:
     - nombre
     - genero
     - tag
     - plataformas
     - fecha de lanzamiento
     - imagen
    """ 
    if request.method == 'POST':
        form = VideoJuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('games') 
    else:
        form = VideoJuegoForm()
    
    contexto = {'form': form}
    return render(request, 'AppGames/forms/video_juegos_form.html', contexto)

# def nuevo_videojuego(request):
#     """
#     Agregar un nuevo juego mediante un form, de acuerdo con el modelo VideoJuego
#     input:
#      - nombre
#      - genero
#      - tag
#      - plataformas
#      - fecha de lanzamiento
#      - imagen
#     """ 
#     if request.method == 'POST':
#         form = VideoJuegoForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('games') 
#     else:
#         form = VideoJuegoForm()
    
#     contexto = {'form': form}
#     return render(request, 'AppGames/forms/video_juegos_form.html', contexto)


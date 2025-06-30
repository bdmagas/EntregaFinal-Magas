from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .models import Plataforma, VideoJuego, Valoracion
from .forms import ValoracionForm, VideoJuegoForm, PlataformaForm
import string

# Create your views here.
def inicio(request):
    return render(request, "AppGames/index.html")

def plataformas(request):
    """
    Se muestran todos los juegos disponibles con opción de selección por plataforma
    """     
    # return render(request, "AppGames/plataformas.html")
    plataformas = Plataforma.objects.all()
    plataforma_id = request.GET.get("plataforma_id")  # ← la busca en la URL
    page_number = request.GET.get('page')

    if plataforma_id:
        videojuegos = VideoJuego.objects.filter(plataformas__id=plataforma_id)
    else:
        videojuegos = VideoJuego.objects.all()

    paginator = Paginator(videojuegos, 6)  # 6 por página
    page_obj = paginator.get_page(page_number)

    # Retorna los videojuegos encontrados x plataforma
    contexto = {
        "plataformas": plataformas,
        "videojuegos": videojuegos,
        "page_obj": page_obj,
        "plataforma_seleccionada": int(plataforma_id) if plataforma_id else None
    }
    return render(request, "AppGames/plataformas.html", contexto)


def video_juegos(request):
    """
    Se muestran todos los juegos disponibles con varias opciones de selección:
        - Letra inicial
        - Genero
        - Tags
    """   
    # return render(request, "AppGames/video_juegos.html")
    juegos = VideoJuego.objects.all()

    letra = request.GET.get('letra')
    tag = request.GET.get('tag')
    genero = request.GET.get('genero')
    page_number = request.GET.get('page')
    
    if letra:
        juegos = juegos.filter(nombre__istartswith=letra)        
    if tag:
        juegos = juegos.filter(tag__iexact=tag)
    if genero:
        juegos = juegos.filter(genero__iexact=genero)
    
    letras = list(string.ascii_uppercase)  # ['A', 'B', 'C', ...]
    tags = VideoJuego.objects.values_list('tag', flat=True).distinct()
    generos = VideoJuego.objects.values_list('genero', flat=True).distinct()

    paginator = Paginator(juegos, 6)  # 6 por página
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
        "page_obj": page_obj,
    }

    return render(request, "AppGames/video_juegos.html", contexto)

def valoraciones(request):
    """
    Se muestran todos los juegos disponibles con opción de selección por calificación
    """  

    estrellas = request.GET.get('estrellas')
    page_number = request.GET.get('page')

    if estrellas:
        valoraciones_list = Valoracion.objects.filter(estrellas=estrellas).order_by('-estrellas')
    else:
        valoraciones_list = Valoracion.objects.all().order_by('-estrellas')

    paginator = Paginator(valoraciones_list, 6)  # 6 por página
    page_obj = paginator.get_page(page_number)

    # Retorna los videojuegos encontrados x valoracion
    contexto = {
        'page_obj': page_obj,
        'filtro_estrellas': estrellas,
    }
    return render(request, 'AppGames/valoraciones.html', contexto)


def nueva_valoracion(request):
    """
    Agregar una nueva review de un juego mediante un form, de acuerdo al modelo Valoracion
    input:
     - videojuego
     - calificacion
     - user_name
     - comentario
    """ 
    if request.method == 'POST':
        form = ValoracionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')  
    else:
        form = ValoracionForm(initial={
            'user_name': request.user.username
        })

    contexto = {'form': form}
    return render(request, 'AppGames/valoracion_form.html', contexto)

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
    return render(request, 'AppGames/video_juegos_form.html', contexto)

def nueva_plataforma(request):
    """
    Agregar una nueva plataforma mediante un form, de acuerdo con el modelo Plataforma
    input:
     - nombre
     - descripcion
    """     
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('platforms') 
    else:
        form = PlataformaForm()
    
    contexto = {'form': form}
    return render(request, 'AppGames/plataforma_form.html', contexto)


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # después de registrarse, va a login
    else:
        form = UserCreationForm()

    contexto = {'form': form}
    return render(request, 'registration/register.html', contexto)

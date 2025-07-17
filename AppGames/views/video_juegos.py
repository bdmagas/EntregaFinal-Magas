from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.db.models import Q, Avg
from ..models import VideoJuego, Valoracion, Favorito
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
        juegos = juegos.filter(Q(nombre__icontains=query)).order_by('nombre')   # busqueda/search
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

    favoritos = []
    if request.user.is_authenticated:
        favoritos = Favorito.objects.filter(usuario=request.user).values_list('juego_id', flat=True)

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
        "favoritos": favoritos,
        "page_obj": page_obj,
    }

    return render(request, "AppGames/video_juegos.html", contexto)

class VideoJuegoListView(ListView):
    """
    Vista para listar todos los juegos.
    """
    model = VideoJuego
    template_name = 'AppGames/forms/video_juego_list.html'
    paginate_by = 15                
    ordering = ['nombre',] 

class VideoJuegoDetailView(DetailView):
    """
    Vista para mostrar los detalles de un juego específico.
    """
    model = VideoJuego
    template_name = 'AppGames/forms/video_juego_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        promedio = Valoracion.objects.filter(juego=self.object).aggregate(prom=Avg('estrellas'))['prom']
        context['promedio_rating'] = promedio or 0
        return context
    
class VideoJuegoCreateView(CreateView):
    """
    Vista para crear un nuevo juego.
    """
    model = VideoJuego
    form_class = VideoJuegoForm
    template_name = 'AppGames/forms/video_juegos_form.html'   # form p/crear o editar juegos
    success_url = '/games/listGames'  # Redirige a la lista de games después de crear uno nuevo
    

class VideoJuegoUpdateView(UpdateView):
    """
    Vista para actualizar un juego existente.
    """
    model = VideoJuego
    form_class = VideoJuegoForm
    template_name = 'AppGames/forms/video_juegos_form.html'   # form p/crear o editar juegos
    success_url = '/games/listGames'      # Redirige a la lista de games después de crear uno nuevo


class VideoJuegoDeleteView(DeleteView):
    """
    Vista para eliminar un juego existente.
    """
    model = VideoJuego
    template_name = 'AppGames/forms/video_juego_delete.html'     # form p/borrar juegos
    success_url = '/games/listGames'      # Redirige a la lista de games después de crear uno nuevo
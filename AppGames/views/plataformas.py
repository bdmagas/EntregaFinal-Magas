from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView # Importamos ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from ..models import Plataforma, VideoJuego
from ..forms import PlataformaForm

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
    return render(request, 'AppGames/forms/plataforma_form.html', contexto)


class PlataformaListView(ListView):
    """
    Vista para listar todos los juegos.
    """
    model = Plataforma
    template_name = 'AppGames/forms/plataforma_list.html'
    paginate_by = 10                
    ordering = ['nombre',] 


class PlataformaDetailView(DetailView):
    """
    Vista para mostrar los detalles de un juego específico.
    """
    model = Plataforma
    template_name = 'AppGames/platforms/plataforma_detail.html'

class PlataformaCreateView(CreateView):
    """
    Vista para crear un nuevo juego.
    """
    model = Plataforma
    fields = ['nombre', 'descripcion']
    template_name = 'AppGames/forms/plataforma_form.html'
    success_url = '/platforms/listPlatforms'  # Redirige a la lista de platforms después de crear uno nuevo
    

class PlataformaUpdateView(UpdateView):
    """
    Vista para actualizar un Plataforma existente.
    """
    model = Plataforma
    fields = ['nombre', 'descripcion']
    template_name = 'AppGames/forms/plataforma_form.html'
    success_url = '/platforms/listPlatforms' 


class PlataformaDeleteView(DeleteView):
    """
    Vista para eliminar un plataforma existente.
    """
    model = Plataforma
    template_name = 'AppGames/forms/plataforma_delete.html'
    success_url = '/platforms/listPlatforms'
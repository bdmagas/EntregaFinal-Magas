from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

    paginator = Paginator(videojuegos, 15)  # 15 por página
    page_obj = paginator.get_page(page_number)

    # Retorna los videojuegos encontrados x plataforma
    contexto = {
        "plataformas": plataformas,
        "videojuegos": videojuegos,
        "page_obj": page_obj,
        "plataforma_seleccionada": int(plataforma_id) if plataforma_id else None
    }
    return render(request, "AppGames/plataformas.html", contexto)

class PlataformaListView(ListView):
    """
    Vista para listar todas las plataformas.
    """
    model = Plataforma
    template_name = 'AppGames/forms/plataforma_list.html'
    paginate_by = 10                
    ordering = ['nombre',] 

class PlataformaCreateView(CreateView):
    """
    Vista para crear una nueva plataforma.
    """
    model = Plataforma
    form_class = PlataformaForm
    template_name = 'AppGames/forms/plataforma_form.html'   # form p/crear o editar plataformas
    success_url = '/platforms/listPlatforms'  # Redirige a la lista de platforms después de crear uno nuevo
    

class PlataformaUpdateView(UpdateView):
    """
    Vista para actualizar un Plataforma existente.
    """
    model = Plataforma
    form_class = PlataformaForm
    template_name = 'AppGames/forms/plataforma_form.html'   # form p/crear o editar plataformas
    success_url = '/platforms/listPlatforms'      # Redirige a la lista de platforms después de crear uno nuevo


class PlataformaDeleteView(DeleteView):
    """
    Vista para eliminar un plataforma existente.
    """
    model = Plataforma
    template_name = 'AppGames/forms/plataforma_delete.html'     # form p/borrar plataformas
    success_url = '/platforms/listPlatforms'      # Redirige a la lista de platforms después de crear uno nuevo
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from ..models import Valoracion
from ..forms import ValoracionForm

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
    return render(request, 'AppGames/forms/valoracion_form.html', contexto)
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from AppGames.views.video_juegos import ver_videojuegos, VideoJuegoListView, VideoJuegoUpdateView, VideoJuegoDeleteView, VideoJuegoCreateView, VideoJuegoDetailView
from AppGames.views.plataformas import plataformas, PlataformaListView, PlataformaCreateView, PlataformaDeleteView, PlataformaUpdateView
from AppGames.views.valoraciones import valoraciones, nueva_valoracion
from AppGames.views.general import inicio, about, toggle_favorito, sitemap

urlpatterns = [
    path('', inicio, name='home'),  # Home
    path('games/', ver_videojuegos, name='games'), # Games Ver/Buscar
    path('games/listGames', VideoJuegoListView.as_view(), name='listGames'), # Listado de juegos
    path('games/addGame', VideoJuegoCreateView.as_view(), name='addGame'), # Agregar juego
    path('games/detail/<int:pk>/', VideoJuegoDetailView.as_view(), name='detailGame'), # Detalles del juego
    path('games/edit/<int:pk>/', VideoJuegoUpdateView.as_view(), name='editGame'),  # Editar
    path('games/delete/<int:pk>/', VideoJuegoDeleteView.as_view(), name='deleteGame'),  # Borrar

    path('games/toggleFavs/<int:juego_id>/', toggle_favorito, name='toggleFavs'),

    path('platforms/', plataformas, name='platforms'), # Plataformas
    path('platforms/listPlatforms', PlataformaListView.as_view(), name='listPlatforms'), # Listado de plataformas
    path('platforms/addNew/', PlataformaCreateView.as_view(), name='addPlatform'),  # Crear nueva
    path('platforms/edit/<int:pk>/', PlataformaUpdateView.as_view(), name='editPlatform'),  # Editar
    path('platforms/delete/<int:pk>/', PlataformaDeleteView.as_view(), name='deletePlatform'),  # Borrar


    path('reviews/', valoraciones, name='reviews'), # Reviews
    path('reviews/addNew', nueva_valoracion, name='addNew'), # Agregar review

    path('about/', about, name='about'), # About me

    path('sitemap/', sitemap, name='sitemap'), # Mapa del sitio

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

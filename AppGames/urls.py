from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from AppGames.views.video_juegos import ver_videojuegos, nuevo_videojuego
from AppGames.views.plataformas import plataformas, nueva_plataforma, PlataformaListView, PlataformaCreateView, PlataformaDeleteView, PlataformaDetailView, PlataformaUpdateView
from AppGames.views.valoraciones import valoraciones, nueva_valoracion
from AppGames.views.general import inicio, about

urlpatterns = [
    path('', inicio, name='home'),  # Home
    path('games/', ver_videojuegos, name='games'), # Games Ver/Buscar
    path('games/addGame', nuevo_videojuego, name='addGame'), # Agregar juego

    path('platforms/', plataformas, name='platforms'), # Plataformas
    # path('platforms/addPlatform', nueva_plataforma, name='addPlatform'), # Agregar plataforma   
    path('platforms/listPlatforms', PlataformaListView.as_view(), name='listPlatforms'), 
    path('platforms/<int:pk>/', PlataformaDetailView.as_view(), name='detailPlatform'),
    path('platforms/addNew/', PlataformaCreateView.as_view(), name='addPlatform'),
    path('platforms/edit/<int:pk>/', PlataformaUpdateView.as_view(), name='editPlatform'),
    path('platforms/delete/<int:pk>/', PlataformaDeleteView.as_view(), name='deletePlatform'),


    path('reviews/', valoraciones, name='reviews'), # Reviews
    path('reviews/addNew', nueva_valoracion, name='addNew'), # Agregar review

    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # path('register/', register, name='register'),
    path('about/', about, name='about'), # About me

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

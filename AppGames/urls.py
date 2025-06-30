from django.urls import path
from django.contrib.auth import views as auth_views
from .views import video_juegos, plataformas, valoraciones, inicio, nueva_valoracion, nuevo_videojuego, nueva_plataforma, register

urlpatterns = [
    path('', inicio, name='home'),  # Home
    path('games/', video_juegos, name='games'), # Games
    path('games/addGame', nuevo_videojuego, name='addGame'), # Agregar juego
    path('platforms/', plataformas, name='platforms'), # Plataformas
    path('platforms/addPlatform', nueva_plataforma, name='addPlatform'), # Agregar plataforma
    path('reviews/', valoraciones, name='reviews'), # Reviews
    path('reviews/addNew', nueva_valoracion, name='addNew'), # Agregar review
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
]
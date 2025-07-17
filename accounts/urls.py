from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import perfil_usuario, editar_perfil, register

urlpatterns = [
    path('perfil/', perfil_usuario, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),    
]

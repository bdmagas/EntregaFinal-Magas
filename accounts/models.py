from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
    
    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return '/static/AppGames/img/avatars/av_default_1.jpg'

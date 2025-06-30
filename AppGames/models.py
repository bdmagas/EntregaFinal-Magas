from django.db import models

# Create your models here.
class Plataforma(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class VideoJuego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    tag = models.CharField(max_length=50)
    plataformas = models.ManyToManyField("Plataforma")  # ahora es plural
    lanzamiento = models.DateField()
    imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)  # para que quede mas lindo

    def __str__(self):
        return self.nombre
    
class Valoracion(models.Model):
    user_name = models.CharField(max_length=50)
    juego = models.ForeignKey(VideoJuego, on_delete=models.CASCADE)
    estrellas = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comentarios = models.CharField(max_length=500)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.juego.nombre} - {self.estrellas} estrellas"
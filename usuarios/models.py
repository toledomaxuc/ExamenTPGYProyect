from django.db import models
from django.db import migrations
from django.contrib.auth.models import User
# Create your models here.
class NuevoUsuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=45)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    contrasena = models.CharField(max_length=10, blank=True, null=True)
    activo = models.IntegerField(null=True)

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)

    
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='img/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + '- by' + self.user.username
#buscador

class Noticia(models.Model):
    PERIODISTA_CHOICES = (
        ('Maria Plaza', 'Maria Plaza'),
        ('Isabel Caro', 'Isabel Caro'),
        ('Cesar Vasquez', 'Cesar Vasquez'),
    )

    CATEGORIA_CHOICES = (
        ('POPULAR', 'POPULAR'),
        ('POLITICA', 'POLITICA'),
        ('DEPORTE', 'DEPORTE'),
    )

    periodista = models.CharField(max_length=100, choices=PERIODISTA_CHOICES)
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES)
    palabra_clave = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100,null=True)
    contenido = models.TextField(null=True)
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)

    def __str__(self):
        return f'{self.periodista} - {self.categoria}'
    

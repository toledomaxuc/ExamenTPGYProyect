from django.db import models
from django.db import migrations
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
# Create your models here.
class NuevoUsuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    username = models.CharField(max_length=20, null=True)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    password1 = models.CharField(max_length=20, blank=True, null=False)
    password2 = models.CharField(max_length=20, blank=True, null=False)
    activo = models.IntegerField(null=True)

    def _str_(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)

    
class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Título"))
    description = models.TextField(blank=True, verbose_name=_("Descripción"))
    imagen = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name=_("Imagen"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Creado"))
    datecompleted = models.DateTimeField(null=True, blank=True, verbose_name=_("Fecha completado"))
    important = models.BooleanField(default=False, verbose_name=_("Importante"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - por ' + self.user.username

    class Meta:
        verbose_name = _("Tarea")
        verbose_name_plural = _("Tareas")
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
    

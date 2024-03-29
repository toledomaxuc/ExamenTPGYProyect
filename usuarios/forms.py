from django import forms
from .models import NuevoUsuario
from .models import Noticia
from django.forms import ModelForm
from .models import Task

class usuarioForm(ModelForm):
    class Meta:
        model = NuevoUsuario
        fields = ("nombre",
                  "apellido_paterno",
                  "apellido_materno",
                  "username",
                  "email",
                  "fecha_nacimiento",
                  "telefono",
                  "direccion",
                  "password1",
                  "password2")
        

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'imagen']        


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'imagen', 'important']
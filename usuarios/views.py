from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView
from .models import Noticia, NuevoUsuario
from django.db.models import Q
from django.views.generic import TemplateView
from .forms import NoticiaForm
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
from django.utils import timezone


# Create your views here.

def index(request):
    context={} 
    return render(request, 'usuarios/index.html', context)

#Funcion de registro
def registro(request):
    if request.method == 'GET':
        #si el metodo es GET, vuelve a registro.html y muestra el formulario
        return render(request, 'usuarios/registro.html', {
            'form': UserCreationForm
        })
    else:
        #Si el metodo es POST, valida ambas contraseñas que sean iguales para pasar a
        #guardar el objeto completo
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])     
                 
                nombre           = request.POST["nombre"]
                aPaterno         = request.POST["paterno"]
                aMaterno         = request.POST["materno"]
                usuario          = request.POST['username']    
                email            = request.POST["email"]
                fechaNac         = request.POST["fechaNac"]
                telefono         = request.POST["telefono"]
                direccion        = request.POST["direccion"]
                password1       = request.POST["password1"]
                password2       = request.POST["password2"]
                activo           = '1'
                #en cada variable, luego en la variable objeto guarda todo juntito
                    
                objeto = NuevoUsuario.objects.create(
                                            nombre=nombre,
                                            apellido_paterno=aPaterno,
                                            apellido_materno=aMaterno,
                                            username=usuario,
                                            email=email,
                                            fecha_nacimiento=fechaNac,
                                            telefono=telefono,
                                            direccion=direccion,
                                            password1=password1,   
                                            password2=password2,                                  
                                            activo=1)
                #lo tira a la base de datos con .save()
                user.save()
                login(request, user)
                return render (request, 'usuarios/iniSesion.html',{
                    'form': UserCreationForm,
                    "error": 'usuario creado exitosamente'
                })
            except IntegrityError:
                return render (request, 'usuarios/registro.html',{
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
    return render (request, 'usuarios/registro.html',{
                    'form': UserCreationForm,
                    "error": 'Las contraseñas no coinciden'
})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('index')


def iniSesion(request):
    if request.method == 'GET':
        return render(request, 'usuarios/iniSesion.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'usuarios/iniSesion.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            # Redirige al usuario a la página de inicio o a otra página que desees
            return redirect('tasks_completed')

class PoliticaView(TemplateView):
    template_name = 'usuarios/POLITICA.html'

class PopularView(TemplateView):
    template_name = 'usuarios/POPULAR.html'

class DeporteView(TemplateView):
    template_name = 'usuarios/DEPORTE.html'

def Formulario(request):
    context={} 
    return render(request, 'usuarios/Formulario.html' , context)

def categoria(request):
    context={} 
    return render(request, 'usuarios/categoria.html' , context)


class BuscarNoticias(ListView):
    model = Noticia
    template_name = 'usuarios/resultados_busqueda.html'
    context_object_name = 'resultados'

    def get_queryset(self):
        query = self.request.GET.get('query')
        queryset = super().get_queryset()

        if query:
            queryset = queryset.filter(
                Q(periodista__icontains=query) |
                Q(categoria__icontains=query) |
                Q(palabra_clave__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('query')
        return context


def buscar(request):
    query = request.GET.get('query')
    query_lower = query.lower()

    if query_lower == 'deporte':
        return redirect('DEPORTE')
    elif query_lower == 'politica':
        return redirect('POLITICA')
    elif query_lower == 'popular':
        return redirect('POPULAR')
    elif query_lower == 'maria' or query_lower == 'maria plaza':
        return redirect('POPULAR')
    elif query_lower == 'isabel' or query_lower == 'isabel caro':
        return redirect('POLITICA')
    elif query_lower == 'cesar' or query_lower == 'cesar vasquez':
        return redirect('DEPORTE')
    else:
        resultados = Noticia.objects.filter(
            Q(periodista__icontains=query) |
            Q(categoria__icontains=query) |
            Q(palabra_clave__icontains=query)
        )
        return render(request, 'usuarios/resultados_busqueda.html', {'resultados': resultados, 'query': query})
    

#CRUD
# 
@login_required
def tasks(request):
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull=True)
    return render(request, 'usuarios/tasks.html', {'tasks': tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'usuarios/tasks.html', {'tasks': tasks})
                
@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'usuarios/create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
             return render(request, 'usuarios/create_task.html', {
                'form': TaskForm,
                'error': 'Por favor provee datos correctos'
            })

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'usuarios/task_detail.html',{'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'usuarios/task_detail.html', {
                'task':task, 'form': form, 'error': "Error updating task "
            })

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method =='POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')
    
@login_required   
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method =='POST':
        task.delete()
        return redirect('tasks')
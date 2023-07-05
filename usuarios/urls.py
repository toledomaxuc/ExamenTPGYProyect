#from django.conf.urls import url
from django.urls import path
from . import views
from .views import BuscarNoticias
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('POLITICA', views.PoliticaView.as_view(), name='POLITICA'),
    path('POPULAR', views.PopularView.as_view(), name='POPULAR'),
    path('DEPORTE', views.DeporteView.as_view(), name='DEPORTE'),
    path('Formulario', views.Formulario, name='Formulario'),
    path('categoria', views.categoria, name='categoria'),
    path('resultados-busqueda/', views.buscar, name='resultados_busqueda'),
    path('periodista', views.periodista, name='periodista'),
    path('logout/', views.cerrar_sesion, name="logout"),
    path('iniSesion/', views.iniSesion, name="iniSesion"),
    path('tasks/', views.tasks, name="tasks"),
    path('tasks_completed/', views.tasks_completed, name="tasks_completed"),
    path('tasks/create/', views.create_task, name="create_task"),
    path('tasks/<int:task_id>/', views.task_detail, name="task_detail"),
    path('tasks/<int:task_id>/complete', views.complete_task, name="complete_task"),
    path('tasks/<int:task_id>/delete', views.delete_task, name="delete_task"),
    path('accounts/', include('django.contrib.auth.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
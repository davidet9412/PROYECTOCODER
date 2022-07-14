from django.urls import  path
from AppCoder.models import Estudiantes
from AppCoder.views import *

urlpatterns = [
    path('curso/', curso),
    path('cursos/', cursos, name = 'cursos'),
    path('profesores/', profesores, name= 'profesores'),
    path('estudiantes/', estudiantes, name= 'estudiantes'),
    path('entregables/', entregables, name= 'entregables'),
    path('formulario/', formulario, name= 'formulario'),
    path('profeform/', profeform, name='profeform'),
    path('busquedacomsion/', busquedaComision,name='busquedaComision'),
    path('buscar/', buscar, name="buscar"),
    path('',inicio, name= 'inicio'),
]
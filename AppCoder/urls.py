from django.urls import  path
from AppCoder.models import Estudiantes
from AppCoder.views import *

urlpatterns = [
    path('curso/', curso),
    path('cursos/', cursos, name = 'cursos'),
    path('profesores/', profesores, name= 'profesores'),
    path('estudiantes/', estudiantes, name= 'estudiantes'),
    path('entregables/', entregables, name= 'entregables'),
    path('',inicio, name= 'inicio'),
]
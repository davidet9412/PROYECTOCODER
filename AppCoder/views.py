from http.client import HTTPResponse
from urllib.error import HTTPError
from django.shortcuts import render
from AppCoder.models import Curso, Profesores
from django.http import HttpResponse
from django.http import HttpRequest
from AppCoder.forms import CursoForm, ProfeForm

# Create your views here.

def curso(self):

    curso=Curso(nombre="Django",comision=939393)
    curso.save()
    texto =f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

def inicio (request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    return render(request, "AppCoder/cursos.html")

def profesores(request):
    return render(request, "AppCoder/profesores.html")

def estudiantes(request):
   return render(request, "AppCoder/estudiantes.html")

def entregables(request):
    return render(request, "Appcoder/entregables.html")

def formulario(request):

    if(request.method == "POST"):

        form = CursoForm(request.POST)  
        
        if form.is_valid():
            info = form.cleaned_data            
            nombre = info["nombre"]
            comision=info["comision"]
            curso = Curso(nombre=nombre, comision=comision)
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form= CursoForm()
    return render(request,"AppCoder/formulario.html",{"formulario":form})    


def profeform(request):

    if(request.method == "POST"):
        form = ProfeForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profe = Profesores(nombre=nombre, apellido= apellido, email = email, profesion = profesion)
            profe.save()
            return render(request, "AppCoder/inicio.html")
    else:
        form = ProfeForm()
    return render(request, "AppCoder/profeform.html", {"profeform":form}) 


def busquedaComision(request):
    return render(request,"AppCoder/busquedacomision.html")

def buscar(request):
    if request.GET["comision"]:

        comision = request.GET["comision"]
        cursos = Curso.objects.filter(comision = comision)
        return render(request, "AppCoder/resultadoBusqeda.html", {"cursos":cursos})

    else:
        return render(request, "AppCoder/busquedacomision", {"error":"No se ingreso ninguna comision "})

# def formulario(request):

#     if(request.method == "POST"):
#         curso = request.POST.get("curso")
#         comision = request.POST.get("comision")
#         curso = Curso(nombre=curso, comision=comision)
#         curso.save()
#         return render(request, "AppCoder/inicio.html") ## Si se guarda bien se devuelve al Inici
#     return render(request, "AppCoder/formulario.html")
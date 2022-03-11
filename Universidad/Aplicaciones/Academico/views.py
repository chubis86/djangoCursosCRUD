from django.shortcuts import render, redirect

from .models import Curso
from django.contrib import messages

# Create your views here.
def home(request):
    cursosListados = Curso.objects.all()
    messages.success(request, '¡Cursos Listados!')
    return render(request, "gestionCursos.html", {"cursos": cursosListados})

def registrarCurso(request):
    """ OBTENEMOS LOS VALORES PROVENIENTES DE gestionCursos.html """
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    """ AGREGAMOS A LA BASE """
    curso = Curso.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos
    )
    messages.success(request, '¡Cursos Registrado!')
    """ REDIRECCIONAMOS PERO NECESITAMOS IMPORTAR redirect """
    return redirect('/')
    """ redireccionamos al directorio raíz """

def edicionCurso(request, codigo):
    curso= Curso.objects.get(codigo=codigo)
    return render(request, "edicionCurso.html", {"curso": curso})

def editarCurso(request):
    """ OBTENEMOS LOS VALORES PROVENIENTES DE edicionCursos.html """
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    creditos=request.POST['numCreditos']

    curso= Curso.objects.get(codigo=codigo)
    curso.nombre= nombre
    curso.creditos= creditos
    curso.save() 

    messages.success(request, '¡Cursos Actualizado!')
    """ REDIRECCIONAMOS PERO NECESITAMOS IMPORTAR redirect """
    return redirect('/')
    """ redireccionamos al directorio raíz """

def eliminarCurso(request, codigo):
    """ OBTENEMOS EL REGISTRO DE LA TABLA PARA POSTERIORMENTE ELIMINARLO """
    curso= Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, '¡Curso Eliminado!')
    """ REDIRECCIONAMOS PERO NECESITAMOS IMPORTAR redirect """
    return redirect('/')
    """ redireccionamos al directorio raíz """

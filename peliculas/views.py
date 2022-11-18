from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def ayuda(request):
    return render(request, 'paginas/ayuda.html')

def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas':peliculas})



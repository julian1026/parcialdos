from django.shortcuts import render
##
from django.views.generic import TemplateView, ListView,CreateView,UpdateView,DeleteView
from .models import Libro
# Create your views here.


class AddCreateView(CreateView):
    template_name = "addlibro.html"
    model=Libro
    fields=('__all__')
    success_url= '/mostrarLibro'

class MostrarLibros(ListView):
    template_name = "mostrarlibros.html"
    context_object_name = 'listar'
    model = Libro
    fields = ('_all_')


class LibroUpdate(UpdateView):
    template_name = "actualizarLibro.html"
    model=Libro
    fields=('__all__')
    success_url='/mostrarLibro'

class LibroDelete(DeleteView):
    template_name = "eliminarLibro.html"
    model=Libro
    fields=('__all__')
    success_url='/mostrarLibro'



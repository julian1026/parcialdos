from django.shortcuts import render
##
from django.views.generic import TemplateView, ListView,CreateView,UpdateView,DeleteView
from .models import Autor
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"



class AddCreateView(CreateView):
    template_name = "addAutor.html"
    model=Autor
    fields=('__all__')
    success_url= '/mostrarAutores'

class MostrarAutores(ListView):
    template_name = "mostrarAutores.html"
    context_object_name = 'listar'
    model = Autor
    fields = ('_all_')

class AutoresUpdate(UpdateView):
    template_name = "actualizarAutor.html"
    model=Autor
    fields=('__all__')
    success_url='/mostrarAutores'

class AutorDelete(DeleteView):
    template_name = "eliminarAutor.html"
    model=Autor
    fields=('__all__')
    success_url='/mostrarAutores'
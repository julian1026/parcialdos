from django.shortcuts import render
##
from django.views.generic import TemplateView, ListView,CreateView,UpdateView,DeleteView
from .models import Prestamo
# Create your views here.

class AddCreateView(CreateView):
    template_name = "addPrestamo.html"
    model=Prestamo
    fields=('__all__')
    success_url= '/mostrarPrestamos'

class MostrarPrestamos(ListView):
    template_name = "mostrarPrestamos.html"
    context_object_name = 'listar'
    model = Prestamo
    fields = ('_all_')

class PrestamoUpdate(UpdateView):
    template_name = "actualizarPrestamos.html"
    model=Prestamo
    fields=('__all__')
    success_url='/mostrarPrestamos'

class PrestamoDelete(DeleteView):
    template_name = "eliminarPrestamo.html"
    model=Prestamo
    fields=('__all__')
    success_url='/mostrarPrestamos'

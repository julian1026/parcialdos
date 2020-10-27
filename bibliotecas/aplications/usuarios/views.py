from django.shortcuts import render
##
from django.views.generic import TemplateView, ListView,CreateView,UpdateView,DeleteView
from .models import Usuario
# Create your views here.

class AddCreateView(CreateView):
    template_name = "addUsuario.html"
    model=Usuario
    fields=('__all__')
    success_url= '/mostrarUsuarios'

class MostrarUSuarios(ListView):
    template_name = "mostrarUsuarios.html"
    context_object_name = 'listar'
    model = Usuario
    fields = ('_all_')

class UsuarioUpdate(UpdateView):
    template_name = "actualizarUsuario.html"
    model=Usuario
    fields=('__all__')
    success_url='/mostrarUsuarios'

class UsuarioDelete(DeleteView):
    template_name = "eliminarUsuario.html"
    model=Usuario
    fields=('__all__')
    success_url='/mostrarUsuarios'

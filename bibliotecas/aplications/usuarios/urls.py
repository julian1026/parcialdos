from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('addUsuarios/', views.AddCreateView.as_view()),
    path('mostrarUsuarios/', views.MostrarUSuarios.as_view()),
    path('actualizarUsuarios/<pk>/', views.UsuarioUpdate.as_view()),
    path('eliminarUsuario/<pk>/', views.UsuarioDelete.as_view()),
]
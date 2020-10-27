from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('addLibro/', views.AddCreateView.as_view()),
    path('mostrarLibro/', views.MostrarLibros.as_view()),
    path('actualizarLibro/<pk>/', views.LibroUpdate.as_view()),
    path('eliminarLibro/<pk>/', views.LibroDelete.as_view()),
]

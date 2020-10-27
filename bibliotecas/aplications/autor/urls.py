from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('addAutor/', views.AddCreateView.as_view()),
    path('home/', views.HomeView.as_view()),
    path('mostrarAutores/', views.MostrarAutores.as_view()),
    path('actualizarAutores/<pk>/', views.AutoresUpdate.as_view()),
     path('eliminarAutores/<pk>/', views.AutorDelete.as_view()),
]

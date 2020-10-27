from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('addPrestamo/', views.AddCreateView.as_view()),
    path('mostrarPrestamos/', views.MostrarPrestamos.as_view()),
    path('actualizarPrestamos/<pk>/', views.PrestamoUpdate.as_view()),
    path('eliminarPrestamo/<pk>/', views.PrestamoDelete.as_view()),
]
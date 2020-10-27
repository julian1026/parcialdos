from django.db import models

from aplications.libro.models import Libro
from aplications.usuarios.models import Usuario
class Prestamo(models.Model):
    Id_prestamo=models.IntegerField()
    Fecha_prestamo=models.CharField(max_length=50)
    Fecha_devolucion=models.CharField(max_length=50)
    Id_libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    Id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)

    
    
    def _str_(self):
        return str(self.Id_prestamo)
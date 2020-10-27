from django.db import models
from aplications.libro.models import Libro

# Create your models here.
class Autor(models.Model):
    idAutor = models.IntegerField()
    nombre = models.CharField(max_length= 100)
    nacionalidad = models.CharField(max_length= 100)
    idLibro= models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idAutor)

from django.db import models

# Create your models here.

class Libro(models.Model):

    idLibro=models.IntegerField()
    codigo=models.IntegerField()
    titulo=models.CharField(max_length=100)
    isbn=models.CharField(max_length=50)
    editorial=models.CharField(max_length=100)
    numPags=models.IntegerField()
    def __str__(self):
        return str(self.idLibro)
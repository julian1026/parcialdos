from django.db import models

# Create your models here.
class Usuario(models.Model):
    Id_usuario=models.IntegerField()
    Num_usuario=models.IntegerField()
    NIF=models.CharField(max_length=50)
    Nombre=models.CharField(max_length=50)
    Direccion=models.CharField(max_length=50)
    Telefono=models.CharField(max_length=50)
    
    def _str_(self):
        return str(self.Id_usuario)
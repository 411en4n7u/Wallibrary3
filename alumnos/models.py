from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=70)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    titulo = models.CharField(max_length=70)
    tipo = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    precio = models.IntegerField()
    autor = models.CharField(max_length=70)
    imagen = models.ImageField(upload_to = "productos", null=True)
    editorial = models.ForeignKey(Editorial, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo

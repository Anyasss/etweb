from django.db import models
from django.utils import timezone

# Create your models here.
class Producto(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    costo_presu = models.IntegerField()
    costo_real = models.IntegerField()
    tienda = models.TextField()
    notas = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.nombre

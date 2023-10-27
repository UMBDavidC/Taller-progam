from django.db import models

# Create your models here.
class Lugares(models.Model):
    name = models.CharField(max_length=250, verbose_name='Nombre chusito')
    address = models.CharField(max_length=250, verbose_name='Dirección')
    lat = models.FloatField(verbose_name='Latitud')
    lng = models.FloatField(verbose_name='Longitud')

class Meta:
    verbose_name = 'chusito'
    verbose_name_plural = 'chusitos'
    ordering = ['name']

def __str__(self):
    return self.name
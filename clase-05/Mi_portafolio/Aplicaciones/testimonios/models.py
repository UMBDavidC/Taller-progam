from django.db import models

class Testimonio(models.Model):
    nombre = models.CharField(max_length=100)
    testimonio = models.CharField( max_length=2000 )
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.nombre


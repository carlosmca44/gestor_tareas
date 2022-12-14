from django.db import models
from django.contrib.auth.models import User


class Tarea(models.Model):
    prioridad = models.IntegerField(default=1)
    tarea = models.CharField(max_length=100)
    fecha_entrega = models.DateField(null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.tarea


class bsElement(models.Model):
    id_number = models.IntegerField(null=True)

    def __str__(self):
        return self.id_number.__str__()

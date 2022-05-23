from django.db import models
from django.utils import timezone
# Create your models here.

class Modelo(models.Model):
    name = models.CharField('Name',max_length=50)
    image = models.URLField('URL for image', default='')
    description = models.CharField('Description', max_length=250, default=None)
    value = models.FloatField('value', default=0.0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Marca(models.Model):
    name_marca = models.CharField('Marca', max_length=300, default='')
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
from django.db import models


class Polera(models.Model):
    nombre_polera = models.CharField(max_length=155)
    precio_polera = models.PositiveIntegerField()
    stock_polera = models.PositiveIntegerField()
    descripcion_polera = models.TextField()
    imagen_polera = models.CharField(max_length=555)

    def __str__(self):
        return self.nombre_polera


class Fragancia(models.Model):
    nombre_fragancia = models.CharField(max_length=155)
    precio_fragancia = models.PositiveIntegerField()
    tipo_fragancia = models.CharField(max_length=55, default='')
    stock_fragancia = models.PositiveIntegerField()
    descripcion_fragancia = models.TextField()
    imagen_fragancia = models.CharField(max_length=555)

    def __str__(self):
        return self.nombre_fragancia
from django.db import models

# Create your models here.

class Tareas(models.Model):
  fecha = models.DateField()
  hora_inicio = models.TimeField(verbose_name="hora de inicio")
  linea = models.CharField(max_length=255, blank=False)
  producto = models.CharField(max_length=255, blank=False)
  trabajadores = models.CharField(max_length=100, blank=False, verbose_name="trabajador")
  producto_terminado = models.CharField(max_length=255, blank=False, verbose_name="producto terminado")
  und_producidas = models.IntegerField(verbose_name="unidades producidas")
  rotulo_fecha_fecha1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="rotulo 1 fecha")
  rotulo_fecha_fecha2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="rotulo 2 fecha")
  hora_termino = models.TimeField(verbose_name="hora de termino")
  cantidad =  models.IntegerField(verbose_name="Cantidad de productos")
  def __str__(self):
    return '{},{},{},{},{},{},{},{},{},{}'.format(
    self.fecha, self.hora_inicio, self.linea, self.producto, self.trabajadores, self.producto_terminado, self.und_producidas, self.hora_termino, self.cantidad)
  
class ProductoA(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class ProductoB(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class ProductoC(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
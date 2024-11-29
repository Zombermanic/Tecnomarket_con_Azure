from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de la marca")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name="Marca"
        verbose_name_plural ="Marcas"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    price = models.IntegerField(verbose_name="Precio")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(upload_to="products", null=True, blank=True, verbose_name="Imagen")
    state = models.BooleanField(verbose_name="¿Es nuevo?")
    manufacturing = models.DateField(verbose_name="Fecha de fabricación")
    brand = models.ForeignKey(Brand, on_delete= models.PROTECT, verbose_name="Marca")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        ordering = ["-created",]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name


from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=200, blank=True, null=True)
    SKU = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Categoria', on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to = 'products', blank=True, null=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.name


class Categoria(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name
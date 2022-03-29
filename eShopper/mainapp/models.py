from django.db import models


class ProductCategory(models.Model):
    '''model for category'''

    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
        ordering = ('name',)

class Product(models.Model):
    '''model for product'''

    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукции'
        ordering = ('name', 'price', 'quantity')

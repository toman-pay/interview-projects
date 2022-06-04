from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=3, max_digits=9)
    description = models.TextField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to='images/', blank=True)

    class Meta:
        verbose_name = 'Product Images'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return self.product.title
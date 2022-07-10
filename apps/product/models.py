import uuid

from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField
from django.db import models

from apps.product.managers import ProductManager


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    search_vector = SearchVectorField(null=True, blank=True)

    owner = models.ForeignKey('user.User', on_delete=models.CASCADE)

    # meta
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    objects = ProductManager()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        indexes = [
            GinIndex(fields=['search_vector']),
        ]
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    @property
    def files_count(self) -> int:
        """
        Count of images for this product
        """
        return self.files.all().count()

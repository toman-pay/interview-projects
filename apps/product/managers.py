from django.contrib.postgres.search import SearchVectorField
from django.db import models


class ProductManager(models.Manager):
    def create(self, title, description, **kwargs):
        search_vector = SearchVectorField(title, description)
        product = self.model(search_vector=search_vector, **kwargs)
        product.save(force_insert=True, using=self.db)
        return product

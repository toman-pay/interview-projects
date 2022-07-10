from django.db import models


class ProductManager(models.Manager):
    def create(self, **kwargs):
        return super().create(**kwargs)

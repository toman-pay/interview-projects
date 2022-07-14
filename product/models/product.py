import uuid
from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title

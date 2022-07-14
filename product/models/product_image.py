from django.db import models

from product.models.validators import validate_file_size
from .product import Product


class ProductImage(models.Model):
    image = models.ImageField(upload_to="image_uploads/", validators=[validate_file_size])
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="images"
    )

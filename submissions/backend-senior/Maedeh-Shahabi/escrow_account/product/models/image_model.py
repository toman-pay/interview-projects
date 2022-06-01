from django.db import models

from escrow_account.models.base_model import BaseModel
from product.models import ProductModel


def images_upload_path(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class ImageModel(BaseModel):
    image_path = models.ImageField(upload_to=images_upload_path, blank=False, null=False, editable=False)
    product_id = models.ForeignKey(to=ProductModel, on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        db_table = "image"

from django.db import models

from escrow_account.models.base_model import BaseModel
from escrow_account.models.uuid_model import UUIDModel
from product.models import ProductModel


def images_upload_path(instance, filename):
    """
    This method returns images storage path
    """
    return 'images/{filename}'.format(filename=filename)


class ImageModel(UUIDModel, BaseModel):
    image = models.ImageField(upload_to=images_upload_path, blank=False, null=False, editable=False)
    product = models.ForeignKey(to=ProductModel, to_field='id', on_delete=models.CASCADE, blank=False, null=False)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        db_table = "image"

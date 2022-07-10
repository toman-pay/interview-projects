from django.db import models

from apps.file.models import AbstractFileModel


class ProductFile(AbstractFileModel):
    """
    File that are belonged to product images.
    To let first image has been upload then process of product creation be done, we can have not any product
        linked to this model.
    """
    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
        null=True,
        default=None,
        related_name='files'
    )

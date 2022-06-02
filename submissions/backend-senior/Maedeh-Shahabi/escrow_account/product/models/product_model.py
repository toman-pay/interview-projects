from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from escrow_account.models.base_model import BaseModel
from escrow_account.models.uuid_model import UUIDModel


class ProductModel(UUIDModel, BaseModel):
    name = models.CharField(max_length=125, null=False, blank=False)
    description = models.TextField(max_length=1024, null=False, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=0, validators=[MinValueValidator(Decimal('0.01'))])

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "product"

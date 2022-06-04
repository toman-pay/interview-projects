from django.db import models
from common.basemodels import BaseModel
from django.utils.translation import gettext_lazy as _
from .utils import product_image_path


class ProductModel(BaseModel):
    """
    This model is used to store product information
    """
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    price = models.DecimalField(_("price"), max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title


class ProductImageModel(BaseModel):
    """
    This model is used to store product photos
    """
    product = models.ForeignKey(ProductModel, verbose_name=_("product"), on_delete=models.CASCADE)
    images = models.ImageField(_("image"), upload_to=product_image_path, null=True , blank=True)

    def __str__(self):
        return self.product.title

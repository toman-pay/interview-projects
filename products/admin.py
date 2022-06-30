from django.contrib import admin

from escrow.models.base_model_admin import BaseModelAdmin
from products.models import ProductImageModel, ProductModel


class ProductImageInline(admin.TabularInline):
    model = ProductImageModel
    max_num = 5


@admin.register(ProductImageModel)
class ProductImageModelAdmin(BaseModelAdmin):
    pass


@admin.register(ProductModel)
class ProductModelAdmin(BaseModelAdmin):
    inlines = [ProductImageInline, ]

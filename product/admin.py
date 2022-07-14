from django.contrib import admin

from .models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price"]


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ["id"]
    raw_id_fields = ["product"]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)

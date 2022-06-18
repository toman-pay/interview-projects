from django.contrib import admin
from product.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]


admin.site.register(Product, ProductAdmin)

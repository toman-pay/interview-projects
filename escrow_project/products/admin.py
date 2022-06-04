from django.contrib import admin

from products.models import Product, ProductImage


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product


@admin.register(ProductImage)
class PostImageAdmin(admin.ModelAdmin):
    pass
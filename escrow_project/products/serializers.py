from rest_framework import serializers

from products.models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('images',)


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(source='productimage_set', many=True, required=False)

    class Meta:
        model = Product
        fields = ('images', 'title', 'price', 'description')



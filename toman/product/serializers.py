from product.models import Product, ProductImage
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = [
            'image'
        ]


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, product):
        """
           return product images
        """
        return ProductImageSerializer(product.images, many=True).data,

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'amount',
            'images',
        ]

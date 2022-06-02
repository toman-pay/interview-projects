from rest_framework import serializers
from .models import Product, ProductMedia
from screw.validations import file_size_validation


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(validators=[file_size_validation], required=False)

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

    def create(self, validated_data):
        validated_data.pop('image')
        product = Product.objects.create(**validated_data)
        return product

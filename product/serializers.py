from rest_framework import serializers

from product.models import Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price"]
        extra_kwargs = {
            "title": {"write_only": True},
            "description": {"write_only": True},
            "price": {"write_only": True},
        }

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except Exception as e:
            raise serializers.ValidationError(str(e))


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]

from django.conf import settings
from rest_framework import serializers

from product.models import Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    imageids = serializers.ListSerializer(
        child=serializers.IntegerField(),
        required=False,
        max_length=settings.MAX_NUMBER_OF_FILES_PER_PRODUCT,
        write_only=True,
    )

    class Meta:
        model = Product
        fields = ["imageids", "id", "title", "description", "price"]
        extra_kwargs = {
            "title": {"write_only": True},
            "description": {"write_only": True},
            "price": {"write_only": True},
        }

    def create(self, validated_data):
        imageids = validated_data.pop("imageids", [])

        try:
            instance = super().create(validated_data)
            ProductImage.objects.filter(id__in=imageids).update(product=instance)
            return instance
        except Exception as e:
            raise serializers.ValidationError(str(e))


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from products.models import ProductImageModel
from products.models import ProductModel

image_count_limit = settings.IMAGE_COUNT_LIMIT
image_byte_size_limit = settings.IMAGE_BYTE_SIZE_LIMIT
image_megabyte_size_limit = settings.IMAGE_MEGABYTE_SIZE_LIMIT


class ImageSerializer(serializers.ModelSerializer):
    """ Image model Serializer """

    class Meta:
        model = ProductImageModel
        fields = [
            'image',
        ]


class SubmitProductSerializer(serializers.ModelSerializer):
    """ Submit new Product model serializer """
    images = ImageSerializer(source='productimagemodel_set', many=True, allow_null=True, read_only=True)

    def validate(self, attrs):
        product_images = self.context.get('view').request.FILES

        # Check images count
        if len(product_images) > image_count_limit:
            raise serializers.ValidationError(
                _(f"You can not upload more than {image_byte_size_limit} images for this products."))

        # Check images size
        for img in product_images.values():
            if img.size > image_byte_size_limit:
                raise serializers.ValidationError(_(f"Image size can not be over {image_megabyte_size_limit} MB."))

        return attrs

    def create(self, validated_data):
        # Create products object first
        product_obj = ProductModel.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            price=validated_data.get('price'))

        # Create products images if exists
        product_images = self.context.get('view').request.FILES
        for img in product_images.values():
            ProductImageModel.objects.create(
                product=product_obj,
                image=img)

        return product_obj

    class Meta:
        model = ProductModel
        fields = [
            'id',
            'title',
            'description',
            'price',
            'images',
        ]

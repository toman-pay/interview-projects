from rest_framework import serializers
from ..models import ProductImageModel, ProductModel
from rest_framework.exceptions import ValidationError
from ..messages import Messages
from django.conf import settings


class ProductSerializer(serializers.ModelSerializer):
    """
    This class is used to serialize input data to create a product
    """
    images = serializers.ListField(
        required=False, child=serializers.ImageField(use_url=True), max_length=settings.MAIMUM_IMAGES_LENGTH)

    class Meta:
        model = ProductModel
        fields = ('title', 'price', 'description', 'images')
        extra_kwargs ={
            'price' : {
                'min_value' : 10 ** -settings.DECIMAL_PLACES,
                'error_messages' : {'min_value' : Messages.MIN_VALUE.value}
            }
        }

    def validate_images(self, value):
        error_value = {}
        for image in value:
            if image.size > settings.MXIMUM_IMAGE_SIZE:
                error_value[image.name] = Messages.IMAGE_SIZE.value
        if error_value:
                raise ValidationError(error_value)
        return value

    def to_representation(self, instance):
        result = {}
        result['success'], result['id'] = 'true', instance.id
        return result
    
    def create(self, validated_data):
        images = validated_data.pop('images', False)
        product_obj = super().create(validated_data)
        if images:
            p = ProductImageModel.objects.bulk_create(
                ProductImageModel(
                    product=product_obj,
                    image=picture
                    ) for picture in images
            )
        return product_obj

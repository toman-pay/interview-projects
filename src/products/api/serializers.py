from rest_framework import serializers
from ..models import ProductImageModel, ProductModel
from rest_framework.exceptions import ValidationError, NotAcceptable
from ..messages import Messages
from django.conf import settings
from django.db import transaction, DatabaseError


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
                'min_value' : 10 ** -(settings.DECIMAL_PLACES +1),
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
        try:
            with transaction.atomic():
                product_obj = super().create(validated_data)
                if images:
                    ProductImageModel.objects.bulk_create(
                        ProductImageModel(
                            product=product_obj,
                            image=picture
                            ) for picture in images
                    )
        except DatabaseError:
            raise NotAcceptable({'error': Messages.DATABASE_ERROR.value})

        return product_obj

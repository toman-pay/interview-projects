from rest_framework import serializers

from product.models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    """
    A serializer for our image model
    """
    class Meta:
        model = ImageModel
        fields = [
            'image',
        ]

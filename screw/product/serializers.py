from rest_framework import serializers
from .models import Product
from screw.validations import file_size_validation, upload_limit_validation


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(validators=[file_size_validation], required=False)

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']

    def validate(self, attrs):
        self.images = self.context.get('files').pop('image', [])
        upload_limit_validation(self.images, 5)
        return attrs

    def create(self, validated_data):
        validated_data.pop('image', [])
        product = Product.objects.create(**validated_data)
        for image in self.images:
            product.media.create(image=image)
        return product

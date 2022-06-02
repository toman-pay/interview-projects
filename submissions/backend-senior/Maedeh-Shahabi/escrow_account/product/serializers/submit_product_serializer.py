from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from product.models import ProductModel, ImageModel
from product.serializers.image_serializer import ImageSerializer


class SubmitProductSerializer(serializers.ModelSerializer):
    """
    A serializer class for creating new product
    """
    images = ImageSerializer(source='imagemodel_set', many=True, allow_null=True, read_only=True)

    def validate(self, attrs):
        product_images = self.context.get('view').request.FILES

        # Validate images count
        if len(product_images) > 5:
            raise serializers.ValidationError(_("You can't upload more than 5 images for this product."))

        # Validate images size, it shouldn't be more than 2 MB
        for _img in product_images.values():
            if _img.size > 2_000_000:
                raise serializers.ValidationError(_("Image size must be under 2 MB."))

        return attrs

    def create(self, validated_data):
        # Create product object first
        product_obj = ProductModel.objects.create(
            name=validated_data.get('name'),
            description=validated_data.get('description'),
            price=validated_data.get('price'))

        # Then create product images if any
        product_images = self.context.get('view').request.FILES
        for _img in product_images.values():
            ImageModel.objects.create(
                product=product_obj,
                image=_img)

        return product_obj

    class Meta:
        model = ProductModel
        fields = [
            'id',
            'name',
            'description',
            'price',
            'images',
        ]

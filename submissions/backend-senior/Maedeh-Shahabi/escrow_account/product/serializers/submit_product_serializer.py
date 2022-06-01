from rest_framework import serializers

from product.models import ProductModel


class SubmitProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            'name',
            'description',
            'price',
            'id',
        ]

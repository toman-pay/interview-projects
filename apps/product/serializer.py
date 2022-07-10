from django.db import transaction
from rest_framework import serializers

from apps.file.serializer import ProductFileSerializer
from apps.product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    images = serializers.ListField(required=False, default=None, write_only=True)
    files = ProductFileSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'owner', 'created_at', 'updated_at', 'files', 'images')
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')

    @transaction.atomic
    def create(self, validated_data):
        from apps.file.models import ProductFile
        images = validated_data.pop("images")
        product = super().create(validated_data)
        if images:
            user = self.context["request"].user
            ProductFile.objects.filter(id__in=images, creator=user, product__isnull=True).update(product=product)
        return product

    @transaction.atomic
    def update(self, instance, validated_data):
        from apps.file.models import ProductFile
        images = validated_data.pop("images")
        product = super().update(instance=instance, validated_data=validated_data)

        if images is not None and isinstance(images, list):
            user = self.context["request"].user
            previous_images = instance.files.all().values_list('id', flat=True)
            removed_images = [i for i in previous_images if i not in images]
            added_images = [i for i in images if i not in previous_images]

            ProductFile.objects \
                .filter(id__in=removed_images, creator=user, product__isnull=False) \
                .update(product=None)

            ProductFile.objects \
                .filter(id__in=added_images, creator=user) \
                .exclude(product=product) \
                .update(product=product)

            product.refresh_from_db()

        return product

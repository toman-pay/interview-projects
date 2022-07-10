from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import serializers

from apps.file.models import ProductFile
from apps.file.utils import sizeof_fmt


class ProductFileSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = ProductFile
        fields = ('id', 'creator', 'original_name', 'core', 'md5sum', 'meta',)
        read_only_fields = ('id', 'original_name', 'creator', 'md5sum', 'meta',)

    def validate_core(self, obj: InMemoryUploadedFile):
        """
        Check if the file size is in our valid range or not.
        Note: Since it is better to check this part on Nginx, we added this limit in Nginx config for this upstream too.
        """
        if obj.size > settings.MAX_UPLOAD_SIZE:
            raise serializers.ValidationError(f"Your file size is {sizeof_fmt(obj.size)} "
                                              f"which is more than {sizeof_fmt(settings.MAX_UPLOAD_SIZE)} limit.")
        return obj

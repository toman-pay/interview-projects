from rest_framework.exceptions import ValidationError
from os import path
from django.utils import timezone
from django.conf import settings


def is_image(ext):
    support_ext = settings.SUPPORTED_IMAGE_FORMATS
    if ext.lower() not in support_ext:
        raise ValidationError('unknown file format')
    return True

def product_image_path(instance, filename):
    ext = filename.split('.')[-1].lower()
    if is_image(ext):
        return path.join('.','images', 'products', '{}.{}'.format(int(timezone.now().timestamp()), ext))
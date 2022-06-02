from django.db import models
import uuid
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import receiver
from django.conf import settings


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=128, unique=True)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.name}"


class ProductMedia(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    image = models.FileField(upload_to=settings.MEDIA_UPLOAD_TO)
    product = models.ForeignKey(Product, related_name='media', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uuid.hex}"


@receiver(pre_save, sender=ProductMedia)
def media_rename(sender, instance, **kwargs):
    if not instance.id:
        instance.image.name = instance.uuid.hex

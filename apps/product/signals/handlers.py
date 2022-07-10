from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.product.models import Product
from apps.product.tasks import update_search_vector


@receiver(post_save, sender=Product)
def remove_file_from_storage(sender, instance: Product, *args, **kwargs):
    update_search_vector.delay(id=instance.id)

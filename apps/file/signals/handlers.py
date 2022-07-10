from django.db.models.signals import pre_delete
from django.dispatch import receiver

from apps.file.models import ProductFile
from apps.file.tasks import remove_file_from_local_storage


@receiver(pre_delete, sender=ProductFile)
def remove_file_from_storage(sender, instance, *args, **kwargs):
    pass

from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver

from apps.file.models import ProductFile
from apps.file.tasks import remove_file_from_local_storage_task


@receiver(post_delete, sender=ProductFile)
def remove_file_from_storage(sender, instance: ProductFile, *args, **kwargs):
    remove_file_from_local_storage_task.delay(path=instance.core.path)

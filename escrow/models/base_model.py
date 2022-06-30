import uuid

from django.db import models
from django.utils import timezone

from escrow.managers import SoftDeletionManager


class BaseModel(models.Model):
    """This model provides some features some uuid field, soft deletion in our project"""
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    pk_id = models.BigAutoField(primary_key=True, editable=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def delete(self):
        """This method actually do soft deletion for objects"""
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        """This method really deletes an object :|"""
        super(BaseModel, self).delete()

    def restore(self):
        """This method restores a deleted object :)"""
        self.deleted_at = None
        self.save()

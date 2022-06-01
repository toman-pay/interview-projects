from django.db import models
from django.utils import timezone

from escrow_account.manager.base_model_manager import BaseModelManager


class BaseModel(models.Model):
    # Soft Deletion
    is_deleted = models.BooleanField(blank=False)
    deletion_time = models.DateTimeField(blank=True, null=True, default=None)

    # override these fields accordingly
    objects = BaseModelManager()
    all_objects = BaseModelManager(alive_only=False)

    # we want to have these fields in every model to log creation time and last update time of an object
    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    class Meta:
        # Abstract Base class inheriting
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """
        It is called on every object's delete method (objects which are inherited from this class)
        """
        self.is_deleted = True
        self.deletion_time = timezone.now()
        self.save()

    def hard_delete(self, using=None, keep_parents=False):
        """
        Call this method when you want to really delete an object!
        """
        super(BaseModel, self).delete(using=using, keep_parents=keep_parents)

    def restore(self):
        """
        Call this method when you want to restore a deleted object.
        """
        self.is_deleted = False
        self.deletion_time = None
        self.save()

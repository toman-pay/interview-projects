from django.db.models import QuerySet
from django.utils import timezone


class SoftDeletionQuerySet(QuerySet):
    """
     In this custom QuerySet class we implement some method based on our soft deletion feature
    """

    def delete(self):
        """
        This method is called when you are bulk deleting a queryset, it'll be called on each object's delete methodt.
        So we should soft delete the object.
        """
        return super(SoftDeletionQuerySet, self).update(
            is_deleted=True,
            deletion_time=timezone.now())

    def hard_delete(self):
        """
        This method is used when you want to do a bulk hard delete on a queryset.
        """
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        """
        Returns a queryset of objects which haven't been deleted.
        """
        return self.filter(deletion_time=None)

    def dead(self):
        """
        Returns a queryset of objects which have been deleted.
        """
        return self.exclude(deletion_time=None)

from django.db.models import QuerySet
from django.utils import timezone


class SoftDeletionQuerySet(QuerySet):
    """ SoftDeletionQuerySet """

    def delete(self):
        """This method is used to do a bulk deleting a queryset."""
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def hard_delete(self):
        """This method is used to do a bulk hard delete on a queryset."""
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        """Returns a queryset of objects which haven't been deleted."""
        return self.filter(deleted_at=None)

    def dead(self):
        """Returns a queryset of objects which have been deleted."""
        return self.exclude(deleted_at=None)

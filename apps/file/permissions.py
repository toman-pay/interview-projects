from rest_framework.permissions import BasePermission


class ProductFileOwnerPermission(BasePermission):
    """
    Object permission for ProductFile.
    Just ProductFile owner can access the product instance.
    """
    @classmethod
    def has_object_permission(cls, request, view, obj):
        return obj.creator == request.user

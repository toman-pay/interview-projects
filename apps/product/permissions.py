from rest_framework.permissions import BasePermission, IsAuthenticated


class ProductOwnerPermission(BasePermission):
    """
    Object permission for product.
    Just product owner can access the product instance.
    """
    @classmethod
    def has_object_permission(cls, request, view, obj):
        return obj.owner == request.user

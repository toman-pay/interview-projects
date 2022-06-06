from rest_framework import mixins, viewsets
from .serializers import ProductSerializer


class ProductViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    This class is used to create the product
    """
    serializer_class = ProductSerializer

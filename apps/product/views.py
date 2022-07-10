from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from apps.product.filters import ProductFilter
from apps.product.models import Product
from apps.product.permissions import ProductOwnerPermission
from apps.product.serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().prefetch_related('files')
    permission_classes = (ProductOwnerPermission,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProductFilter

    def get_queryset(self):
        if self.action.lower() == 'list':
            return self.queryset.filter(owner=self.request.user)
        return super(ProductViewSet, self).get_queryset()

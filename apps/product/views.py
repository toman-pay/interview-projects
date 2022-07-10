from django.shortcuts import render
from rest_framework import viewsets

from apps.product.models import Product
from apps.product.permissions import ProductOwnerPermission
from apps.product.serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().prefetch_related('files')
    permission_classes = (ProductOwnerPermission, )

    def get_queryset(self):
        if self.action.lower() == 'list':
            return self.queryset.filter(owner=self.request.user)
        return super(ProductViewSet, self).get_queryset()

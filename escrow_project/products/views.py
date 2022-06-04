from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(ViewSet, GenericViewSet):
    """ Escrow Products ViewSet """
    permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        """ list of products endpoint """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """ retrieve product based on product id endpoint """
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """ create product endpoint """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data['title'], status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        """ delete product endpoint """
        product = self.get_object()
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import ProductSerializer, ProductImageSerializer


class CreateProductView(CreateAPIView):
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        is_valid = serializer.is_valid(raise_exception=False)
        if is_valid:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {"success": True, **serializer.data},
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CreateProductImageView(CreateAPIView):
    serializer_class = ProductImageSerializer

from rest_framework.viewsets import GenericViewSet
from django.db.transaction import atomic
from rest_framework.response import Response
from product.serializers import ProductSerializer


class ProductView(GenericViewSet):
    serializer_class = ProductSerializer

    @atomic
    def create(self, request):
        """
        Create product, image_objects and return a list of UUIDs.
        """
        form = self.serializer_class(data=request.data, context={'files': request.FILES})
        if form.is_valid():
            product = form.save()
            return Response({'status': 201, 'id': product.uuid.hex}, 201)
        return Response({'status': 400, 'message': form.errors}, 400)

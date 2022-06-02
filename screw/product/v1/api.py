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
        form = self.serializer_class(data=request.data)
        if form.is_valid():
            images_data = request.FILES.pop('image')
            if len(images_data) < 6 or None:
                product = form.save()
                for image in images_data:
                    product.media.create(image=image)
                return Response({'status': 201, 'id': product.uuid.hex}, 201)
            else:
                return Response({'status': 400, 'message': 'Sorry! maximum number of images to upload is 5'}, 400)
        return Response({'status': 400, 'message': form.errors}, 400)

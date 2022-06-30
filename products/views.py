from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from escrow.utils import create_response_data
from products.models import ProductModel
from products.serializers import SubmitProductSerializer


class SubmitProductView(CreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = SubmitProductSerializer

    parser_classes = (
        MultiPartParser,
        FormParser,
    )

    def post(self, request, *args, **kwargs):
        serializer: SubmitProductSerializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer=serializer)
            success = True
            id = serializer.data.get('id')
            data = dict()
            status_code = status.HTTP_201_CREATED


        else:
            success = False
            id = None
            data = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST

        response_data = create_response_data(success=success, id_=id, data=data)

        return Response(data=response_data, status=status_code)

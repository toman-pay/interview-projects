from typing import Any, Dict, Optional

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from escrow_account.base_constants import BaseConstants
from escrow_account.utils.response_utils import ResponseUtils
from product.models import ProductModel
from product.serializers.submit_product_serializer import SubmitProductSerializer


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
            data: dict = dict()
            _status_code: str = status.HTTP_201_CREATED
            success: bool = True
            id_: Optional[str] = serializer.data.get(BaseConstants.id_)

        else:
            data: dict = serializer.errors
            _status_code: str = status.HTTP_400_BAD_REQUEST
            success: bool = False
            id_: Optional[str] = None

        final_data: Dict[str, Any] = ResponseUtils().get_create_response_data(
            success=success,
            id_=id_,
            data=data)

        return Response(data=final_data, status=_status_code)

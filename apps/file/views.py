from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from apps.file.models.product_file_model import ProductFile
from apps.file.permissions import ProductFileOwnerPermission
from apps.file.serializer import ProductFileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = ProductFile.objects.all()
    http_method_names = ['post', 'get', 'delete']
    serializer_class = ProductFileSerializer
    permission_classes = (ProductFileOwnerPermission, )

    def get_queryset(self, **kwargs):
        if self.action.lower() == 'list':
            return self.queryset.filter(creator=self.request.user)
        return super().get_queryset()

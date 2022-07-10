from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser
from apps.file.models.product_file_model import ProductFile
from apps.file.serializer import ProductFileSerializer


class FileViewSet(viewsets.ModelViewSet):
    # parser_classes = (FileUploadParser,)
    queryset = ProductFile.objects.all()
    http_method_names = ['post', 'get', 'delete']
    serializer_class = ProductFileSerializer

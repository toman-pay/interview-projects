from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from interview_task.utils import response
from product.models import Product, ProductImage
from product.serializers import ProductSerializer

from product.validators import validate_image_size


@permission_classes((IsAuthenticated,))
class CreateProductView(APIView):
    """ This method is use to submit a new Product """

    def post(self, request):
        """
            Product registration
        """
        images = request.data.getlist("images")
        validate_image_size(images) # checking image size
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product = product_serializer.save()
            for image in images:
                if ProductImage.allowed_image_count(product.id):
                    continue
                ProductImage.objects.create(
                    product_id=product.id,
                    image=image,
                )

            return response(product_serializer.data, "product added successfully", True, 200)
        return response(product_serializer.errors, "Bad request.", False, 400)


@permission_classes((IsAuthenticated,))
class ProductDetailsView(APIView):
    """ This method is use to getting Product details """

    def get(self, request):
        """
            Getting product list and filtering on ID
        """
        products = Product.objects.all().order_by("created_at")
        product_id = request.GET.get("id", None)
        if product_id:
            product = products.filter(id=product_id).first()
            product_serializer = ProductSerializer(product)
        else:
            product_serializer = ProductSerializer(products, many=True)
        return response(product_serializer.data)

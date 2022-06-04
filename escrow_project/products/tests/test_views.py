from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.authtoken.models import Token

from products.models import Product, ProductImage
from products.views import ProductViewSet


client = APIClient()


class ProductTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.valid_payload = {
            'title': 'test 3',
            'price': '1000',
            'description': 'test description',
        }
        self.invalid_payload = {
            'title': 'test 4',
            'price': 'bs price',
            'description': 'test description',
        }
        self.product_i = Product.objects.create(
            title='test 1',
            price=1000,
            description='test description'
        )
        self.product_image_i = ProductImage.objects.create(
            product=self.product_i,
            images='test.jpg'
        )
        self.product_ii = Product.objects.create(
            title='test 2',
            price=1000,
            description='test description'
        )
        self.product_image_ii = ProductImage.objects.create(
            product=self.product_ii,
            images='test.jpg'
        )
        self.user_i = User.objects.create(
            email='test@gmail.com',
            password='1234'
        )
        self.token = Token.objects.create(user=self.user_i)
        self.client.login(email=self.user_i.email, password=self.user_i.password)
        self.client.force_authenticate(user=self.user_i)

    def test_products_list(self):
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], self.product_i.title)
        self.assertEqual(response.data[1]['title'], self.product_ii.title)

    def test_product_retrieve(self):
        product_iii = Product.objects.create(
            id=1000,
            title='test 1000',
            price=1000,
            description='test description'
        )
        response = self.client.get('/api/v1/products/1000', follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], product_iii.title)

    def test_product_valid_create(self):
        response = self.client.post('/api/v1/products/',
                                    data=self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_product_invalid_create(self):
        response = self.client.post('/api/v1/products/',
                                    data=self.invalid_payload,
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_product_delete(self):
        response = self.client.delete('/api/v1/products/2/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

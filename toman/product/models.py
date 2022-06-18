from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.image.name

    @staticmethod
    def allowed_image_count(product_id):
        """
            Checking the product image count
        """
        image_count = ProductImage.objects.filter(product_id=product_id).count()
        return True if image_count >= 5 else False

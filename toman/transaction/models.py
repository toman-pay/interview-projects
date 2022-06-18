from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product


class Transaction(models.Model):
    reference_id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_success = models.BooleanField(default=False)
    message = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

from celery import shared_task
from django.contrib.postgres.search import SearchVector


@shared_task
def update_search_vector(id):
    from apps.product.models import Product
    Product.objects.filter(id=id).update(
        search_vector=SearchVector('title', 'description')
    )

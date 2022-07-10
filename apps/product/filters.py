from django_filters import rest_framework as filters

from apps.product.models import Product


class ProductFilter(filters.FilterSet):
    search = filters.CharFilter(field_name="search_vector")
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Product
        fields = ['title', 'description', 'created_at', 'updated_at', 'search']

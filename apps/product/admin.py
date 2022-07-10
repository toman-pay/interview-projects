from django.contrib import admin

from apps.file.models import ProductFile
from apps.product.models import Product


class ProductFileTabularInline(admin.TabularInline):
    model = ProductFile
    readonly_fields = (
        'id', 'original_name', 'md5sum', 'meta', 'creator', 'is_optimized', 'removed_from_storage', 'core'
    )


class ProductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'the_description', 'files_count',)
    inlines = (ProductFileTabularInline,)
    list_filter = ('created_at',)
    search_fields = ('=search_vector',)

    def get_search_results(self, request, queryset, search_term):
        """
        Custom search using postgresql tsvector
        """
        if search_term:
            return queryset.filter(search_vector=search_term), False
        return queryset, False

    def the_description(self, instance: Product):
        return "".join(instance.description[:50]) + " ..." if isinstance(instance.description, str) else ''


admin.site.register(Product, ProductionAdmin)

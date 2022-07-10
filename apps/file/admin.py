from django.contrib import admin

from apps.file.models import ProductFile


class ProductFileAdmin(admin.ModelAdmin):
    date_hierarchy = 'create_date'
    list_display = ('id', 'creator', 'original_name', 'is_public', 'is_optimized', 'create_date')
    search_fields = ['uuid', 'creator__username']
    # raw_id_fields = ('product', 'creator')
    list_filter = ('is_public', 'is_optimized', 'create_date')
    readonly_fields = ('original_name', 'is_public', 'is_optimized', 'create_date', 'creator', 'md5sum', 'meta')


admin.site.register(ProductFile, ProductFileAdmin)

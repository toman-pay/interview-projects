# from django.contrib import admin
# from django.utils.html import format_html
#
# from apps.my_admin.admin import admin_site
# from .models import File
#
#
# class FileAdmin(admin.ModelAdmin):
#     date_hierarchy = 'create_date'
#     list_display = ('uuid', 'is_public', 'is_optimized', 'filesize', 'create_date', 'image_view')
#     search_fields = ['uuid', 'creator__username']
#     raw_id_fields = ('klass', 'creator', 'conversation',)
#     list_filter = ('is_public', 'is_optimized', 'create_date')
#
#     readonly_fields = ('image_view',)
#
#     def image_view(self, obj):
#         return format_html(
#             '<img style="width:50px" src="{}">',
#             obj.link,
#         )
#
#
# admin_site.register(File, FileAdmin)

from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    """This model admin is matched with BaseModel to supporting soft deletion feature"""

    def get_queryset(self, request):
        queryset = self.model.all_objects
        # The below is copied from the base implementation in BaseModelAdmin to prevent other changes in behavior
        ordering = self.get_ordering(request)
        if ordering:
            queryset = queryset.order_by(*ordering)
        return queryset

    def delete_model(self, request, obj):
        obj.hard_delete()

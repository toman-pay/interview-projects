from django.contrib import admin
from transaction.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):

    list_display = [
        'user',
        'is_success',
        'reference_id',
        'message',
        'created_at',
    ]

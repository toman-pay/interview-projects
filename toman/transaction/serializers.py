from transaction.models import Transaction
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = [
            'user',
            'is_success',
            'message',
            'reference_id',
            'product_id',
            'created_at',
        ]

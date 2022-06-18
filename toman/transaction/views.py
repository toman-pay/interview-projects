from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from interview_task.utils import response

from transaction.serializers import TransactionSerializer
from transaction.models import Transaction


@permission_classes((IsAuthenticated,))
class OrderProductView(APIView):
    """ This method is use to pay a Product """

    def post(self, request):
        request_data = request.data.copy()
        request_data["user"] = request.user.id
        transaction_serializer = TransactionSerializer(data=request_data)
        if transaction_serializer.is_valid():
            transaction = transaction_serializer.save()
            # In the actual case this be done after the payment operation not here
            transaction.is_success = True
            transaction.message = "your request was successfully registered"
            transaction.save()
            return response(transaction_serializer.data, "the payment was successfully", True, 200)
        return response(transaction_serializer.errors, "Bad request.", False, 400)


@permission_classes((IsAuthenticated,))
class TransactionDetailsView(APIView):
    """ This method is use to getting Transaction details """

    def get(self, request):
        """
            Getting transaction list and filtering on ID
        """
        transactions = Transaction.objects.all().order_by("created_at")
        transaction_id = request.GET.get("id", None)
        if transaction_id:
            transaction = transactions.filter(id=transaction_id).first()
            transaction_serializer = TransactionSerializer(transaction)
        else:
            transaction_serializer = TransactionSerializer(transactions, many=True)
        return response(transaction_serializer.data)

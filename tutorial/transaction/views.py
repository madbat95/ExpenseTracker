from requests import Response
from rest_framework import permissions
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework.views import APIView
from transaction.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import permissions, status
from django.http import Http404



class TransactionList(APIView):
    """
    List all transactions, or create a new transaction.
    """
    def get(self, request, format=None):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransactionDetail(APIView):
    """
    View account Details and provide functionality for update, delete and read
    """
    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except Transaction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

   

    
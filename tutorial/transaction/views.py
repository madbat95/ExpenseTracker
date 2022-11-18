from requests import Response
from rest_framework import permissions
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
from rest_framework import generics
from rest_framework import viewsets
from transaction.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions




class TransactionList(generics.ListCreateAPIView):    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save()

class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    #this will a read-write-delete endpoint for each individual account
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
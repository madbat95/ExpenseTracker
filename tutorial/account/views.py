from django.shortcuts import render

# Create your views here.
from account.models import Account
from account.serializers import AccountSerializer
from rest_framework import generics

from account.models import Account


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
from django.shortcuts import render
from rest_framework import permissions
# Create your views here.
from account.models import Account
from account.serializers import AccountSerializer
from rest_framework import generics

from account.models import Account
from .permissions import IsOwnerOrReadOnly



class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrReadOnly]
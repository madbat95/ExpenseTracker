from rest_framework import generics
from .models import Account
from .serializers import AccountSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly

class AccountList(generics.ListCreateAPIView):
    #this will create a read and write endpoint that lists all available Account instances 
    
    
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    #this will a read-write-delete endpoint for each individual account
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
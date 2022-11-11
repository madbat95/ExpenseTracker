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


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'accounts': reverse('account-list', request=request, format=format),
        'transactions': reverse('transaction-list', request=request, format=format)
    })

class TransactionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
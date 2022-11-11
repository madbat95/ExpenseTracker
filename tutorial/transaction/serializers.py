from rest_framework import serializers
from .models import Transaction
from account.models import Account


class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    account = serializers.ReadOnlyField(source = 'account.name') 
    class Meta:
        model = Transaction
        fields = ['account_id', 'transaction_id', 'transaction_choices', 
                    'transaction_type', 'category', 'description', 'amount', 'date', 'account']

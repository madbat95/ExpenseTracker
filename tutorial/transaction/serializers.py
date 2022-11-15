from rest_framework import serializers
from .models import Transaction
from account.models import Account


class TransactionSerializer(serializers.ModelSerializer):
    #account_id = serializers.ReadOnlyField(source = 'account.account_id') 
    class Meta:
        model = Transaction
        fields = ['account_id', 'transaction_id', 'transaction_type', 'category', 'description', 'amount', 'date'] # , 'account']

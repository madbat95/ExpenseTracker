#TRANSACTION

from rest_framework import serializers

from .models import Transaction
#from account.models import Account


class TransactionSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Transaction
        fields = ['transaction_id','account', 'transaction_type', 'category',
         'description', 'amount', 'date',] 

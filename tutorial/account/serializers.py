#ACCOUNT
from rest_framework import serializers
from account.models import Account
from django.contrib.auth import get_user_model
from transaction.serializers import TransactionSerializer
from transaction.models import Transaction
#from transaction.models import Transaction

class AccountSerializer(serializers.ModelSerializer):
    
    #account_transactions = TransactionSerializer(read_only = True, many=True) 
    #account_transactions = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())

    class Meta:
        model = Account
        fields = ('account_id', 'name', 'owner', ) #'account_transactions']  # 'transactions']



class AccountDetailSerializer(serializers.ModelSerializer):
    account_transactions = TransactionSerializer(many=True)

    class Meta:
        model = Account
        fields = ('account_id', 'name', 'account_transactions')
        extra_kwargs = {
           'account_id': {'read_only': True},
            'name': {'read_only': True},
            'account_transactions': {'read_only': True},
        }
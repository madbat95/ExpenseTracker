#ACCOUNT
from rest_framework import serializers
from account.models import Account
from django.contrib.auth import get_user_model

from transaction.serializers import TransactionSerializer
from transaction.models import Transaction
#from transaction.models import Transaction
User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='User.username') #THIS IS REDUNDANT
    #account_transactions = TransactionSerializer(read_only = True, many=True) 
    #account_transactions = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())

    class Meta:
        model = Account
        fields = ['account_id', 'name', 'owner'] #'account_transactions']  # 'transactions']


    # def create(self, validated_data):
    #     account_transactions = self.account_transactions
    #     transactions_data = validated_data.pop(account_transactions)
    #     account = Account.objects.create(**validated_data)
    #     for transaction_data in transactions_data:
    #         Account.objects.create(account=account, **transaction_data)
    #     return account

    # def update(self, instance, validated_data):
    #     account_transactions = self.account_transactions
    #     transaction_data = validated_data.pop(account_transactions)
    #     transactions = (instance.account_transactions).all()
    #     transactions = list(transactions)
    #     instance.account_id = validated_data.get('account_id', instance.account_id)
    #     instance.owner = validated_data.get('owner', instance.owner)
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()

    #     for transaction in account_transactions:
    #         transaction = transactions.pop(0)
    #         transaction.account = transaction_data.get('account', transaction.account)
    #         transaction.transaction_id = transaction_data.get('transaction_id', transaction.transaction_id)
    #         transaction.transaction_type = transaction_data.get('transaction_type', transaction.transaction_type)
    #         transaction.category = transaction_data.get('category', transaction.category)
    #         transaction.description = transaction_data.get('description', transaction.description)
    #         transaction.amount = transaction_data.get('amount', transaction.amount)
    #         transaction.date = transaction_data.get('date', transaction.date)
    #         transaction.save()
    #     return instance
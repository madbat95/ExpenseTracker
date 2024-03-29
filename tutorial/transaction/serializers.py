#TRANSACTION

from rest_framework import serializers

from .models import Transaction
#from account.models import Account


class TransactionSerializer(serializers.ModelSerializer):
    transaction_type = serializers.IntegerField(required=True)
    #account = serializers.PrimaryKeyRelatedField(many=True, queryset=Transaction.objects.all())
    category = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


    class Meta:
        model = Transaction
        fields = ('transaction_id','account', 'transaction_type', 'category',
         'description', 'amount', 'date') 
        extra_kwargs = {
            'transaction_id': {'read_only': True},
            'account': {'read_only': True},
            'transaction_type': {'read_only': True},#, 'allow_blank': False},
            'category': {'read_only': True},#, 'allow_blank': False},
            'description': {'read_only': True},
            'amount': {'read_only': True},# 'allow_blank': False},
            'date': {'read_only': True},
        }
from rest_framework import serializers
from account.models import Account
from django.contrib.auth import get_user_model
#from transaction.models import Transaction
User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='User.username') 
    #transactions = serializers.HyperlinkedRelatedField(many=True, view_name='transaction-view', read_only=True) 

    class Meta:
        model = Account
        fields = ['account_id', 'name', 'owner']  # 'transactions']


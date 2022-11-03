from rest_framework import serializers
from account.models import Account
from user.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_id', 'user_id', 'name', 'user']

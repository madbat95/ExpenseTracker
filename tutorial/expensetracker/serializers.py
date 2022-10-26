from rest_framework import serializers
from expensetracker.models import Account, User, Transaction


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_id', 'name', 'user_name', 'email', 'dob']


class AccountSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['account_id', 'user_id', 'name']



# class transactionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Transaction
#         fields = ['account_id', 'transaction_id', 'transaction_choices', 'transaction_type', 'category', 'description', 'amount', 'date']
        
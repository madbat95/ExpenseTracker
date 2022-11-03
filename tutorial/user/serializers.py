from rest_framework import serializers

from tutorial.account.models import Account
from .models import User


class UserSerializer(serializers.ModelSerializer):
    accounts = serializers.PrimaryKeyRelatedField(many=True, query = Account.objects.all()) 

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name',
                  'dob', 'accounts')
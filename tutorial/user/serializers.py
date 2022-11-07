from rest_framework import serializers

from account.models import Account
from .models import User


class UserSerializer(serializers.ModelSerializer):
    accounts = serializers.PrimaryKeyRelatedField(many=True, queryset = Account.objects.all()) 

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name',
                  'dob', 'accounts')
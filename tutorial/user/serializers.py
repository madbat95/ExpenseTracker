from rest_framework import serializers

from account.models import Account
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    accounts = serializers.HyperlinkedRelatedField(many=True, view_name='account-detail', read_only=True) 

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name',
                  'dob', 'accounts']
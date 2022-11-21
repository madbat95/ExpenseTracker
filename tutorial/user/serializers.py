#USER

from rest_framework import serializers
from account.models import Account
from django.contrib.auth import get_user_model

from account.serializers import AccountSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    #accounts = AccountSerializer(many=True) #, queryset=Account.objects.all()) 

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name',
                  'dob')
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'email': {'read_only': True},
            'name': {'read_only': True},
            'dob': {'read_only': False},
        }

class UserDetailSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True) #, queryset=Account.objects.all()) 

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name',
                  'dob', 'accounts')
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'email': {'read_only': True},
            'name': {'read_only': True},
            'dob': {'read_only': False},
            'accounts': {'read_only': True},
        }
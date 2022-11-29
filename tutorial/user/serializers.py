#USER

import email
from rest_framework import serializers
from account.models import Account
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from account.serializers import AccountSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    #accounts = AccountSerializer(many=True) #, queryset=Account.objects.all()) 
   # id = serializers.IntegerField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)
    dob = serializers.DateField(required=True)
    password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', #'id',
                  'dob', 'password')
        extra_kwargs = {
            'id': {'read_only': True},
            'username': {'read_only': True},
            'email': {'read_only': True},
            'name': {'read_only': True},
            'dob': {'read_only': False},
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        # validated_data['password'] = make_password(validated_data['password'])
        # return super(UserSerializer, self).create(validated_data)
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserDetailSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True) 

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
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', 'id', 'username', 'email', 'name',
                  'dob')
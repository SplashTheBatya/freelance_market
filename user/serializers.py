from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from .models import *


# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'role')
        extra_kwargs = {
            'password': {'write_only': True},
        }

        def create(self, validated_data):
            user = MyUser.objects.create_user(validated_data['username'], password=validated_data['password'],
                                              first_name=validated_data['first_name'],
                                              last_name=validated_data['last_name'], role=validated_data['role'])
            return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import Address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'first_name', 'last_name', 'phone']
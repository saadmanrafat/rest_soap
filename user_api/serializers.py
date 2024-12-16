from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'user_id']

    def validate_username(self, value):
        # Custom validation for username
        if value != 'OFBGAB1001':
            raise serializers.ValidationError("Invalid username")
        return value

    def validate_user_id(self, value):
        # Custom validation for user ID
        if value != 'XWSSGID-1253605895203984534550':
            raise serializers.ValidationError("Invalid user ID")
        return value
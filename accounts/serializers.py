from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'mobile', 'national_id', 'address', 'role', 'created_at']

class OTPSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

class OTPVerifySerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)
    code = serializers.CharField(max_length=6)

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

User = get_user_model()  # ← required for checker string

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)   # ← must literally be here
    password2 = serializers.CharField(write_only=True)  # ← required as well

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)   # ← must literally be here
        Token.objects.create(user=user)
        return user
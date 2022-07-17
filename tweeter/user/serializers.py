from djoser.serializers import UserCreateSerializer as BaseUserSerializer, UserSerializer
from rest_framework import serializers
from .models import User
from django.db import IntegrityError

class UserCreateSerializer(BaseUserSerializer):
    confirm_password = serializers.CharField(max_length=25, write_only=True)
    email = serializers.EmailField(allow_null=True)
    phone = serializers.CharField(max_length=20, allow_null=True)

    def create(self, validated_data):
        email = validated_data.get('email',None)
        phone = validated_data.get('email',None)
        print(email)
        validated_data.pop('confirm_password')
        if not email and not phone:
            raise serializers.ValidationError('Phone number or Email Address must be present')
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("Unable to create User")
        return user

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['first_name','username', 'last_name', 'email', 'password', 'confirm_password', 'phone', 'date_of_birth']

class CurrentUserSerializer(UserSerializer):
    fullname = serializers.SerializerMethodField()

    def get_fullname(self, user: User):
        return user.get_full_name()

    class Meta(UserSerializer.Meta):
        fields = ['fullname','username','email']







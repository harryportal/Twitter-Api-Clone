from rest_framework import serializers
from django.conf import settings

class CreateUser(serializers.ModelSerializer):
    confirm_password = serializers.CharField()

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['first_name','last_name','email','password', 'confirm_password']

    def validate_password(self):
        if password != self.confirm_password:
            raise serializers.ValidationError('Password must match')
        return password



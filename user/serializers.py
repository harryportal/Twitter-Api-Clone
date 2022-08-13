from djoser.serializers import UserCreateSerializer as BaseUserSerializer, UserSerializer
from rest_framework import serializers
from .models import User
from django.db import IntegrityError
from django.db.models import Count
from tweeter.utils import format_date_created


class UserCreateSerializer(BaseUserSerializer):
    id = serializers.IntegerField(read_only=True)
    confirm_password = serializers.CharField(max_length=25, write_only=True)
    email = serializers.EmailField(allow_null=True)
    phone = serializers.CharField(max_length=20, allow_null=True)

    def create(self, validated_data):
        email = validated_data.get('email', None)
        phone = validated_data.get('email', None)
        print(email)
        validated_data.pop('confirm_password')
        if not email and not phone:
            raise serializers.ValidationError('Phone number or Email Address must be present')
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError("User Exists with ID")
        return user

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('Passwords do not match')
        return attrs

    class Meta(BaseUserSerializer.Meta):
        model = User
        fields = ['id','first_name', 'username', 'last_name', 'email', 'password', 'confirm_password',
                  'phone', 'date_of_birth']


class BaseUserSerializer(serializers.ModelSerializer):
    """ to be used for displaying followers or tweets users """
    fullname = serializers.SerializerMethodField()

    def get_fullname(self, user: User):
        return user.get_full_name()

    class Meta:
        model = User
        fields = ['id', 'username', 'profile_picture', 'fullname', 'bio']


class CurrentUserSerializer(UserSerializer):
    fullname = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    tweets_count = serializers.SerializerMethodField()
    profile_picture = serializers.ImageField()  # configure a different view for image upload
    cover_picture = serializers.ImageField()

    def get_fullname(self, user: User):
        return user.get_full_name()

    def get_date_created(self, user: User):
        return format_date_created(user)

    def get_followers(self, user: User):
        followers = user.followers.count()
        return followers

    def get_following(self, user: User):
        following = user.following.count()
        return following

    def get_tweets_count(self, user: User):
        return user.tweets.count()

    class Meta(UserSerializer.Meta):
        model = User
        fields = ['id', 'fullname', 'username', 'email', 'profile_picture', 'cover_picture', 'bio',
                  'location', 'website', 'date_created', 'followers', 'following', 'tweets_count']


class Followerserializer(serializers.Serializer):
    id = serializers.IntegerField()

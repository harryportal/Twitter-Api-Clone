from rest_framework import serializers
from .models import Comment
from tweeter.utils import format_date_created
from tweeter_api.models import Tweet
from user.serializers import BaseUserSerializer

class ViewCommentSerializer(serializers.ModelSerializer):

    def get_date_created(self, comment: Comment):
        return format_date_created(comment)

    def validate(self, attrs):
        """ ensures the user posts a least a picture or text when tweeting"""
        image = attrs.get('image')
        content = attrs.get('content')
        tweet_id = self.context['tweet_id']
        if not image and not content:
            raise serializers.ValidationError(detail='cannot post an empty comment')
        tweet = Tweet.objects.filter(pk=tweet_id).exists()
        if not tweet:
            raise serializers.ValidationError(detail='No tweets with specified id')
        return attrs

    def create(self, validated_data):
        tweet = Tweet.objects.get(pk=self.context['tweet_id'])
        instance = Comment.objects.create(user=self.context['user'],tweet=tweet, **validated_data)
        return instance

    class Meta:
        model = Comment
        fields = ['content','image']

class CommentSerializer(serializers.ModelSerializer):
    user = BaseUserSerializer()

    class Meta:
        model = Comment
        fields = ['user','image','content','likes','created_at']
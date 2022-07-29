from rest_framework import serializers
from .models import Tweet
from tweeter.utils import format_date_created
from user.serializers import BaseUserSerializer
from comments.serializers import CommentSerializer


class CreateTweetSerializer(serializers.ModelSerializer):
    content = serializers.CharField(max_length=400, required=False)
    image = serializers.ImageField(required=False)

    def validate(self, attrs):
        """ ensures the user posts a least a picture or text when tweeting"""
        image = attrs.get('image')
        content = attrs.get('content')
        if not image and not content:
            raise serializers.ValidationError(detail='cannot post an empty tweet')
        return attrs

    def create(self, validated_data):
        instance = Tweet.objects.create(user=self.context['user'], **validated_data)
        return instance

    class Meta:
        model = Tweet
        fields = ['content','image']

class TweetUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        """ Returns only this details for a individual tweets user"""
        fields = ['id','username','profile_picture','fullname']

class TweetsSerializer(serializers.ModelSerializer):
    user = TweetUserSerializer()
    likes_count = serializers.IntegerField()
    comments_count = serializers.IntegerField()
    date_created = serializers.SerializerMethodField()
    retweets_count = serializers.IntegerField()
    comments = CommentSerializer(many=True)

    def get_date_created(self, tweet: Tweet):
        """ This returns the date (day and month) and add the year only if it's not the current year"""
        return format_date_created(tweet)

    class Meta:
        model = Tweet
        fields = ['id','user','content','image','likes_count','date_created',
                  'comments_count','retweets_count','comments']


class ReTweetsSerializer(serializers.ModelSerializer):
    retweets = BaseUserSerializer(many=True)

    class Meta:
        model = Tweet
        fields = ['retweets']

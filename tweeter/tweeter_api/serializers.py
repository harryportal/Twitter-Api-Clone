from rest_framework import serializers
from .models import Tweet
from tweeter.utils import format_date_created
from user.serializers import TweetsUserSerializer
from comments.serializers import ViewCommentSerializer
from user.serializers import TweetsUserSerializer

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


class UserTweetsSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField()
    comments_count = serializers.IntegerField()
    date_created = serializers.SerializerMethodField()
    retweets_count = serializers.IntegerField()
    comments = ViewCommentSerializer(many=True)

    def get_date_created(self, tweet: Tweet):
        """ This returns the date (day and month) and add the year only if it's not the current year"""
        return format_date_created(tweet)

    class Meta:
        model = Tweet
        fields = ['content','image','likes_count','date_created', 'comments',
                  'comments_count','retweets_count']

class ReTweetsSerializer(serializers.ModelSerializer):
    retweets = TweetsUserSerializer(many=True)

    class Meta:
        model = Tweet
        fields = ['retweets']

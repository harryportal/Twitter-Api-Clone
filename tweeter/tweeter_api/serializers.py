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

class AllTweetsSerializer(serializers.ModelSerializer):
    user = TweetUserSerializer()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    date_created = serializers.SerializerMethodField()
    retweets_count = serializers.SerializerMethodField()
    user_liked = serializers.SerializerMethodField()  # a field to check if the current user has liked the tweet

    def get_date_created(self, tweet: Tweet):
        """ This returns the date (day and month) and add the year only if it's not the current year"""
        return format_date_created(tweet)

    def get_likes_count(self, tweet: Tweet):
        return tweet.likes.count()

    def get_retweets_count(self, tweet: Tweet):
        return tweet.retweets.count()

    def get_comments_count(self, tweet: Tweet):
        return tweet.comments.count()

    def get_user_liked(self, tweet: Tweet): # checks if the current user has liked the post
        return self.context['user'] in tweet.likes.all()

    class Meta:
        model = Tweet
        fields = ['id','user','content','image','likes_count','date_created',
                  'comments_count','retweets_count','user_liked']

class TweetsSerializer(AllTweetsSerializer):
    comments = CommentSerializer(many=True)

    class Meta(AllTweetsSerializer.Meta):
        fields = ['id','user','content','image','likes_count','date_created',
                  'comments_count','retweets_count','user_liked','comments']

class ReTweetsSerializer(serializers.ModelSerializer):
    retweets = BaseUserSerializer(many=True)

    class Meta:
        model = Tweet
        fields = ['retweets']

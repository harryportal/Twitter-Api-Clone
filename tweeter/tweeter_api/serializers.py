from rest_framework import serializers
from .models import Tweet
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


    class Meta:
        model = Tweet
        fields = ['content','image','likes_count','parent','date_created']

from rest_framework import serializers
from .models import Comment
from tweeter.utils import format_date_created

class ViewCommentSerializer(serializers.ModelSerializer):
    def get_date_created(self, comment: Comment):
        return format_date_created(comment)

    class Meta:
        model = Comment
        fields = ['image','content','likes','comments', 'created_at','retweets']
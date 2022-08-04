from django.db import models
from django.conf import settings
from tweeter_api.models import Tweet


User = settings.AUTH_USER_MODEL

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='comments/images', blank=True, null=True)
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=350, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='comments_likes')
    comments = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    retweets = models.ManyToManyField('self')
    date_created = models.DateTimeField(auto_now_add=True)

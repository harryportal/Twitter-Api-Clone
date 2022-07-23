from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    parent = models.ForeignKey('self', related_name='retweets',null=True, on_delete=models.SET_NULL)
    content = models.CharField(max_length=400, null=True, blank=True)
    user = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tweets/images', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through=TweetLike, related_name='likes')








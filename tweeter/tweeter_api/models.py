from django.db import models
from django.conf import settings
from django.db.models import Count,Q

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    date_liked = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    retweets = models.ManyToManyField(User, related_name='retweets')
    content = models.CharField(max_length=400, null=True, blank=True)
    user = models.ForeignKey(User, related_name='tweets', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tweets/images', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, through=TweetLike, related_name='likes')



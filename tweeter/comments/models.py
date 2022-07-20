from django.db import models
from django.conf import settings
from tweeter_api.models import Tweet


User = settings.AUTH_USER_MODELS
class Comments(models.Model):
    user = models.ManyToManyField(User, related_name='comments')
    image = models.ImageField(upload_to='comments/images')
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=350)
    likes = models.ManyToManyField(User, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

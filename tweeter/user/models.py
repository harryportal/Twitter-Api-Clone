from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(max_length=500, null=True)
    image = models.ImageField(upload_to='tweeter_api/images')
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20, null=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, null=True,
                                       related_name='followers')






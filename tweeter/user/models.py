from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='tweeter_api/images')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, null=True,
                                       related_name='followers')
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20)





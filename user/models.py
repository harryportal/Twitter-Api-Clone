from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import Manager, Q


class User(AbstractUser):
    date_created = models.DateField(auto_now_add=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(max_length=500, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    cover_picture = models.ImageField(blank=True, null=True)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=100,null=True)
    website = models.URLField(null=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, related_name='followers')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username}'








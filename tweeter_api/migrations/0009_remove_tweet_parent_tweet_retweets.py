# Generated by Django 4.0.6 on 2022-07-25 16:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweeter_api', '0008_alter_tweet_content_alter_tweet_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='parent',
        ),
        migrations.AddField(
            model_name='tweet',
            name='retweets',
            field=models.ManyToManyField(related_name='retweets', to=settings.AUTH_USER_MODEL),
        ),
    ]
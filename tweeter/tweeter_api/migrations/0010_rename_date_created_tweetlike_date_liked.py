# Generated by Django 4.0.6 on 2022-07-29 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter_api', '0009_remove_tweet_parent_tweet_retweets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweetlike',
            old_name='date_created',
            new_name='date_liked',
        ),
    ]

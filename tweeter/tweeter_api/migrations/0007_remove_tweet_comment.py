# Generated by Django 4.0.6 on 2022-07-23 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweeter_api', '0006_tweet_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='comment',
        ),
    ]

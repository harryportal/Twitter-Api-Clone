# Generated by Django 4.0.6 on 2022-08-04 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0010_alter_comment_content_alter_comment_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='date_created',
        ),
    ]

from django.db import models
from django.conf import settings

user = settings.AUTH_USER_MODEL
class Conversation(models.Model):
    initiator = models.ForeignKey(user, on_delete=models.SET_NULL, null=True,
                         related_name='convo_starter')
    receiver = models.ForeignKey(user, on_delete=models.SET_NULL, null=True,
                         related_name='convo_participant')
    start_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(user, on_delete=models.SET_NULL, null=True,
                         related_name='message_sender')
    text = models.CharField(max_length=200, blank=True)
    attachment = models.FileField(blank=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='message')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-timestamp',)
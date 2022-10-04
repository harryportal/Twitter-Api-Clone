from user.serializers import ChatSerializer
from .models import Conversation, Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('conversation_id',)


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = ChatSerializer()
    receiver = ChatSerializer()
    last_message = serializers.SerializerMethodField()

    def get_last_message(self, instance):
        message = instance.message.first()
        return MessageSerializer(instance=message)

class ConversationSerializer(serializers.ModelSerializer):
    initiator = ChatSerializer()
    receiver = ChatSerializer()
    message = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'message']

from django.shortcuts import render
from .models import Conversation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User
from .serializers import ConversationSerializer, ConversationListSerializer
from django.db.models import Q
from django.shortcuts import redirect, reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_conversation(request, ):
    data = request.data
    username = data.pop('username')
    try:
        participant = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'message': 'User does not exist'}, status=404)
    conversation = Conversation.objects.filter(Q(initiator=request.user, reciever=participant) |
                                               Q(initiator=participant, receiver=request.user))
    if conversation.exists():
        return redirect(reverse('get_conversation', args=conversation[0].id))
    else:
        conversation = Conversation.objects.create(initiator=request.user, receiver=participant)
        serializer = ConversationSerializer(instance=conversation)
        return Response(serializer.data)

@api_view(['GET'])
def get_conversation(request,convo_id):
    conversation = Conversation.objects.filter(id=convo_id)
    if not conversation.exists():
        return Response({'message':'conversation does not exist'}, status=404)
    else:
        serializer = ConversationSerializer(instance=conversation[0])
        return Response(serializer.data)

@api_view(['GET'])
def conversations(request):
    conversation_list = Conversation.objects.filter(Q(initiator=request.user)|Q(receiver=request.user))
    serializer = ConversationListSerializer(instance=conversation_list, many=True)
    return Response(serializer.data)





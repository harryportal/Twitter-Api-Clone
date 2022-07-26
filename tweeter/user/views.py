from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import BaseUserSerializer, Followerserializer
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics



@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def following(request):
    """ follow or unfollow a user"""
    serializer = Followerserializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user_id = serializer.data.get('id')
    user = get_object_or_404(User, pk=user_id)
    following = request.user.following  # people the current user are following
    if user in following.all():
        following.remove(user)
    else:
        following.add(user)
    return Response(serializer.data, status.HTTP_204_NO_CONTENT)

class getFollowers(generics.ListAPIView):
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        followers = user.followers.all()
        return followers
    serializer_class = BaseUserSerializer
    permission_classes = [IsAuthenticated]

class getFollowing(generics.ListAPIView):
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        following = user.following.all()
        return following
    serializer_class = BaseUserSerializer
    permission_classes = [IsAuthenticated]
























from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import BaseUserSerializer, Followerserializer, CurrentUserSerializer
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class Following(APIView):
    def post(self, request):
        """ follow or unfollow a user"""
        serializer = Followerserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data.get('id')
        user = get_object_or_404(User, pk=user_id)
        following = self.request.user.following  # people the current user are following
        if user in following.all():
            following.remove(user)
        else:
            following.add(user)
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)
    permission_classes = [IsAuthenticated]

class getFollowers(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serialiazer = BaseUserSerializer(user.followers.all(), many=True)
        return Response(serialiazer.data)
    permission_classes = [IsAuthenticated]

class getFollowing(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serialiazer = BaseUserSerializer(user.following.all(), many=True)
        return Response(serialiazer.data)
    permission_classes = [IsAuthenticated]

class UserProfile(APIView):
    def get(self, request,pk):
        user = get_object_or_404(User, pk=pk)
        serializer = CurrentUserSerializer(user)
        return Response(serializer.data)
    permission_classes = [IsAuthenticated]

























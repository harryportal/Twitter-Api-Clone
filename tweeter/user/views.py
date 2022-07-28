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
        current_user = self.request.user
        serializer = Followerserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data.get('id')
        if user_id == current_user.id:  # ensure the user cannnot follow the same user
            return Response({'error': 'User cannot follow the same user'}, 400)
        user = get_object_or_404(User, pk=user_id)  # work on a decorator for this later
        following = current_user.following  # people the current user are following
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
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = CurrentUserSerializer(user)
        return Response(serializer.data)

    permission_classes = [IsAuthenticated]

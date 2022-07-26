from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import BaseUserSerializer, Followerserializer
from rest_framework.response import Response
from .models import User
from django.shortcuts import get_object_or_404
from rest_framework import status

class Followers(APIView):
    def get(self, request):
        """ gets a list of users followed """
        following = self.request.user.following
        serializer = BaseUserSerializer(following, many=True)
        return Response(serializer.data)

    def post(self, request):
        """ follow or unfollow a user"""
        serializer = Followerserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data.get('id')
        user = get_object_or_404(User, pk=user_id)
        following = self.request.user.following # people the current user are following
        if user in following.all():
            following.remove(user)
        else:
            following.add(user)
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)













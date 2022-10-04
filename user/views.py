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
from user.utils import get_user
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q


class Following(APIView):
    def post(self, request):
        """ FOLLOW OR UNFOLLOW A USER """
        current_user = self.request.user
        serializer = Followerserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data.get('id')
        if user_id == current_user.id:  # ensure the user cannnot follow the same user
            return Response({'error': 'User cannot follow the same user'}, 400)
        user = get_user(User, user_id)
        if user[0] is False:
            return user[1]  # returns the 404 error specified in the get_object function
        following = current_user.following  # people the current user are following
        user = user[1]  # the user object returned from the list
        if user in following.all():
            following.remove(user)
        else:
            following.add(user)
        return Response(serializer.data, status.HTTP_204_NO_CONTENT)

    permission_classes = [IsAuthenticated]


class getFollowers(APIView):
    def get(self, request, pk):
        """ GET USERS FOLLOWERS WITH USER_ID """
        user = get_user(User, pk)
        if user[0] is False:
            return user[1]
        serialiazer = BaseUserSerializer(user[1].followers.all(), many=True)
        return Response(serialiazer.data)

    permission_classes = [IsAuthenticated]


class getFollowing(APIView):
    def get(self, request, pk):
        """ GET USERS FOLLOWING WITH USER_ID """
        user = get_user(User, pk)
        if user[0] is False:
            return user[1]
        serialiazer = BaseUserSerializer(user[1].following.all(), many=True)
        return Response(serialiazer.data)

    permission_classes = [IsAuthenticated]


class UserProfile(APIView):
    """ GET A USER PROFILE """

    def get(self, request, pk):
        user = get_user(User, pk)
        if user[0] is False:
            return user[1]
        serializer = CurrentUserSerializer(user[1])
        return Response(serializer.data)

    permission_classes = [IsOwnerOrReadOnly]


@api_view(['GET'])
def search_users(request, name):
    """ To search for a user with username, firstname or lastname"""
    # convert the string to a list
    name_query = set(name.split())  # since repititions won't obviously be needed
    if len(name_query) > 4:
        return Response({'message':'Lenght of search query exceeded'}, status.HTTP_400_BAD_REQUEST)
    print(name_query)
    for name in name_query:
        # loop through the set and return
        user = User.objects\
            .filter(Q(username__icontains=name) | Q(first_name__icontains=name) | Q(last_name__icontains=name))\
            .all()
        if user:
            serializer = BaseUserSerializer(user, many=True)
            print(serializer)
            return Response(serializer.data, status.HTTP_200_OK)
    return Response({'message':'No result Found'}, status.HTTP_200_OK)

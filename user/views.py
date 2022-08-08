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

    permission_classes = [IsAuthenticated]

@api_view(['POST'])
def upload_profile_pic(request):
    current_user = request.user
    image_file = request.FILES['image_file']
    image_type = request.POST['image_type']
    if settings.USE_S3:
        user.profile_picture = image_file
        upload = Upload(file=image_file)
        upload.save()
        image_url = upload.file.url
    else:
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        image_url = fs.url(filename)
    return Response({'message':'image succesfully uploaded'},status.HTTP_200_OK)





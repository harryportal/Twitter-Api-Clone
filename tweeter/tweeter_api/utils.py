from rest_framework.response import Response
from .models import Tweet
from rest_framework import status

def get_tweet(pk):
    """ an utility function to get the current user or return a json response if user does not exist"""
    try:
        instance = Tweet.objects.get(pk=pk)
    except Tweet.DoesNotExist:
        return [False, Response({"error":"Tweet does not exist"}, status.HTTP_404_NOT_FOUND)]
    return [True, instance]
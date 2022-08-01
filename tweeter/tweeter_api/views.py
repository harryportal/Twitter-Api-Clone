from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from .serializers import CreateTweetSerializer, TweetsSerializer, ReTweetsSerializer, AllTweetsSerializer, \
    TweetUserSerializer
from .models import Tweet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.models import User
from .utils import get_tweet
from rest_framework.viewsets import ModelViewSet


class UserTweetsViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    """ The update mixin was not added since tweeter currently does not support editing a tweet"""

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AllTweetsSerializer
        elif self.request.method == 'POST':
            return CreateTweetSerializer

    def get_queryset(self):
        queryset = Tweet.objects.filter(user=self.request.user).prefetch_related('retweets')
        return queryset

    def get_serializer_context(self):
        return {'user': self.request.user}

    permission_classes = [IsAuthenticated]


class AllTweetsViewSet(ListAPIView):
    def get_queryset(self):
        """ displays all tweets by the current user and the users followed """
        current_user = self.request.user
        tweets = Tweet.objects.filter(Q(user=current_user) | Q(user__in=current_user.following.all()))
        return tweets

    def get_serializer_context(self):
        return {'user':self.request.user }
    serializer_class = AllTweetsSerializer
    permission_classes = [IsAuthenticated]



class TweetsViewSet(RetrieveAPIView):
    def get_serializer_context(self):
        return {'user': self.request.user}
    queryset = Tweet.objects.all()
    serializer_class = TweetsSerializer
    permission_classes = [IsAuthenticated]




class Retweets(APIView):
    def get(self, request, pk):
        tweet = get_tweet(pk)
        if tweet[0] is False:
            return tweet[1]
        serializer = ReTweetsSerializer(tweet[1])
        return Response(serializer.data)

    def post(self, request, pk):
        user = request.user
        tweet = get_tweet(pk)
        if tweet[0] is False:
            return tweet[1]
        retweets = tweet[1].retweets
        if user in retweets.all():
            retweets.remove(user)
        else:
            retweets.add(user)
        return Response({'message': 'success'})

    permission_classes = [IsAuthenticated]


class Like(APIView):
    def get(self, request, pk):
        """ returns the number of likes and those that liked a tweet"""
        tweet = get_tweet(pk)
        if tweet[0] is False:
            return tweet[1]
        serializer = TweetUserSerializer(tweet[1].likes, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        """ like or unlike a post of already liked"""
        tweet = get_tweet(pk)
        if tweet[0] is False:
            return tweet[1]
        user = self.request.user
        tweet = tweet[1]
        if user in tweet.likes.all():
            tweet.likes.remove(user)
        else:
            tweet.likes.add(user)
        return Response(status.HTTP_200_OK)

    permission_classes = [IsAuthenticated]

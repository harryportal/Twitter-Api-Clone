from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from .serializers import CreateTweetSerializer, TweetsSerializer, ReTweetsSerializer
from .models import Tweet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from .permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserTweetsViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    """ The update mixin was not added since tweeter currently does not support editing a tweet"""

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TweetsSerializer
        elif self.request.method == 'POST':
            return CreateTweetSerializer

    def get_queryset(self):
        queryset = Tweet.tweets.filter(user=self.request.user)
        return queryset

    def get_serializer_context(self):
        return {'user': self.request.user}

    permission_classes = [IsAuthenticated]


class AllTweetsViewSet(ListAPIView):
    def get_queryset(self):
        """ displays all tweets by the current user and the users followed """
        current_user = self.request.user
        tweets = Tweet.tweets.filter(Q(user=current_user) | Q(user__in=current_user.following.all()))
        return tweets
    serializer_class = TweetsSerializer
    permission_classes = [IsAuthenticated]


class TweetViewSet(APIView):
    def get(self, request, pk):
        tweet = Tweet.tweets.get(pk=pk)
        serializer = TweetsSerializer(tweet)
        return Response(serializer.data)

    permission_classes = [IsAuthenticated]


class Retweets(APIView):
    def get(self,request,pk):
        tweets = Tweet.objects.get(pk=pk)
        serializer = ReTweetsSerializer(tweets)
        return Response(serializer.data)

    def post(self,request,pk):
        user = request.user
        retweets = Tweet.objects.get(pk=pk).retweets
        if user in retweets.all():
            retweets.remove(user)
        else:
            retweets.add(user)
        return Response({'message':'success'})



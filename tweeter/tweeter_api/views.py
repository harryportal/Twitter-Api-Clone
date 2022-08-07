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
    """ CREATE,RETREIVE,DELETE AND VIEW YOUR TWEETS """

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


class AllTweetsViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """ VIEW ALL PUBLICLY AVAIALABLE TWEETS """
    def get_queryset(self):
        current_user = self.request.user
        # tweets = Tweet.objects.filter(Q(user=current_user) | Q(user__in=current_user.following.all()))
        tweets = Tweet.objects.all()
        """not using the above query cos it makes the api boring since people can see all \
        tweets except they follow another account"""
        return tweets

    def get_serializer_context(self):
        return {'user': self.request.user}

    def get_serializer_class(self):
        pk = self.kwargs.get('pk')
        return TweetsSerializer if pk else AllTweetsSerializer

    permission_classes = [IsOwnerOrReadOnly]


class Retweets(APIView):
    def get(self, request, pk):
        """ GET USERS THAT RETWEETED A TWEET"""
        tweet = get_tweet(pk)
        if tweet[0] is False:
            return tweet[1]
        serializer = ReTweetsSerializer(tweet[1])
        return Response(serializer.data)

    def post(self, request, pk):
        """ RETWEET OR UNRETWEET """
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
        """ GET USERS THAT LIKED A TWEET """
        tweet = get_tweet(pk)
        if tweet[0] is False:
            return tweet[1]
        serializer = TweetUserSerializer(tweet[1].likes, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        """ LIKE OR UNLIKE A TWEET """
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

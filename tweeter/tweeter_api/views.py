from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from .serializers import CreateTweetSerializer, UserTweetsSerializer, ReTweetsSerializer
from .models import Tweet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q
from .permissions import IsOwnerOrReadOnly


class UserTweetsViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):
    """ The update mixin was not added since tweeter currently does not support editing a tweet"""

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserTweetsSerializer
        elif self.request.method == 'POST':
            return CreateTweetSerializer

    def get_queryset(self):
        queryset = Tweet.objects.filter(user=self.request.user).prefetch_related('retweets'). \
            annotate(likes_count=Count('likes'), comments_count=Count('comments'),
                     retweets_count=Count('retweets'))
        return queryset

    def get_serializer_context(self):
        return {'user': self.request.user}

    permission_classes = [IsAuthenticated]

class AllTweetsViewSet(ListModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    def get_queryset(self):
        """ displays all tweets by the current user and the users followed """
        current_user = self.request.user
        tweets = Tweet.objects.filter(Q(user=current_user) | Q(user__in=current_user.following.all())).\
            prefetch_related('retweets').annotate(likes_count=Count('likes'), comments_count=Count('comments'),
                                                  retweets_count=Count('retweets'))
        return tweets

    serializer_class = UserTweetsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

class RetweetsViewSet(ListModelMixin, GenericViewSet):
    def get_queryset(self):
        queryset = Tweet.objects.get(pk=self.kwargs['tweet_pk']).retweets
        return queryset

    def get_serializer_context(self):
        return {'user': self.request.user}

    serializer_class = ReTweetsSerializer
    permission_classes = [IsAuthenticated]




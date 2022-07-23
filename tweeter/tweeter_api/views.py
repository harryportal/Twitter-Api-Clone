from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from .serializers import CreateTweetSerializer, UserTweetsSerializer
from .models import Tweet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count



class UserTweetsViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    """ The update mixin was not added since tweeter currently does not support editing a tweet"""
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserTweetsSerializer
        elif self.request.method == 'POST':
            return CreateTweetSerializer

    def get_queryset(self):
        queryset = Tweet.objects.filter(user=self.request.user).\
            annotate(likes_count=Count('likes'))
        return queryset

    def get_serializer_context(self):
        return {'user':self.request.user}

    permission_classes = [IsAuthenticated]


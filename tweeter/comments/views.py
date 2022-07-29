from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Comment
from .serializers import ViewCommentSerializer
from rest_framework.permissions import IsAuthenticated


class CommentsViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = ViewCommentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'user':self.request.user,'tweet_id':self.kwargs['id']}


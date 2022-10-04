from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Comment
from .serializers import ViewCommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwnerOrReadOnly


class CommentsViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet,RetrieveModelMixin):
    queryset = Comment.objects.all()
    serializer_class = ViewCommentSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]

    def get_serializer_context(self):
        return {'user':self.request.user,'tweet_id':self.kwargs['tweet_id']}

    # The below logic can be replaced with an extra IsownerorReadonly permision class
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     if instance.user != self.request.user:  # ensure comments can only be deleted by the author
    #         return Response({"error":"comment does not belong to user"}, status.HTTP_404_NOT_FOUND)
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)




from .views import CommentsViewSet
from django.urls import path, include
from rest_framework_nested import routers

app_name = 'comments'
router = routers.DefaultRouter()
router.register('', CommentsViewSet)

urlpatterns = [
    path('<int:tweet_id>/',include(router.urls))
]
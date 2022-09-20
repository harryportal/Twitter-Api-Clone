from rest_framework  import routers
from . import views
from django.urls import path,include
app_name = 'tweets'

router = routers.DefaultRouter()
router.register('me', views.UserTweetsViewSet, basename='mytweet')
router.register('',views.AllTweetsViewSet, basename='tweets')


urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/retweets/', views.Retweets.as_view(), name='retweets'),
    path('<int:pk>/likes/',views.Like.as_view(), name='likes')
]
from rest_framework_nested import routers
from . import views
from django.urls import path,include

app_name = 'tweets'

router = routers.DefaultRouter() # using default routers provides a base url
router.register('tweets', views.UserTweetsViewSet, basename='tweet')

tweet_router = routers.NestedSimpleRouter(router, 'tweets', lookup='tweet')
tweet_router.register('retweets', views.RetweetsViewSet, basename='tweet_retweets')


urlpatterns = [
    path('', include(router.urls)),
    path('',include(tweet_router.urls))
]
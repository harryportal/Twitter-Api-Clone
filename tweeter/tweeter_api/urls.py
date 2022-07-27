from rest_framework_nested import routers
from . import views
from django.urls import path,include

app_name = 'tweets'

router = routers.DefaultRouter() # using default routers provides a base url
router.register('me', views.UserTweetsViewSet, basename='my_tweet')
router.register('all', views.AllTweetsViewSet, basename='all_tweet')

alltweets_router = routers.NestedSimpleRouter(router, 'all', lookup='all_tweet')
mytweets_router = routers.NestedSimpleRouter(router, 'me', lookup='my_tweet')

mytweets_router.register('retweets', views.RetweetsViewSet, basename='mytweet_retweets')
alltweets_router.register('retweets', views.RetweetsViewSet, basename='alltweet_retweets')



urlpatterns = [
    path('', include(router.urls)),
    path('',include(mytweets_router.urls)),
    path('', include(alltweets_router.urls))
]
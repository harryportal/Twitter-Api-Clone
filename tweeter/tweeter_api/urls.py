from rest_framework_nested import routers
from . import views
from django.urls import path,include

app_name = 'tweets'

router = routers.DefaultRouter() # using default routers provides a base url
router.register('me', views.UserTweetsViewSet, basename='tweet')


# alltweets_router = routers.NestedSimpleRouter(router, 'all', lookup='tweet')
# mytweets_router = routers.NestedSimpleRouter(router, 'me', lookup='weet')
#
# mytweets_router.register('retweets', views.RetweetsViewSet, basename='tweet_retweets')
# alltweets_router.register('retweets', views.RetweetsViewSet, basename='tweet_retweets')



urlpatterns = [
    path('', include(router.urls)),
    path('all/',views.AllTweetsViewSet.as_view(), name='alltweets'),
    path('<int:pk>/', views.TweetViewSet.as_view(), name='tweet'),
    path('<int:pk>/retweets', views.Retweets.as_view(), name='retweets')
    # path('',include(mytweets_router.urls)),
    # path('', include(alltweets_router.urls))
]
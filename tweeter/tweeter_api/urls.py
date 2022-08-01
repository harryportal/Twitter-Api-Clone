from rest_framework_nested import routers
from . import views
from django.urls import path,include

app_name = 'tweets'

router = routers.DefaultRouter()
router.register('me', views.UserTweetsViewSet, basename='tweet')


urlpatterns = [
    path('', include(router.urls)),
    path('all/',views.AllTweetsViewSet.as_view(), name='alltweets'),
    path('<int:pk>/', views.TweetsViewSet.as_view(), name='tweet'),
    path('<int:pk>/retweets/', views.Retweets.as_view(), name='retweets'),
    path('<int:pk>/likes/',views.Like.as_view(), name='likes')
]
from rest_framework_nested import routers
from . import views
from django.urls import path,include

app_name = 'tweets'

router = routers.DefaultRouter() # using default routers provides a base url
router.register('tweet', views.UserTweetsViewSet, basename='tweet')


urlpatterns = [
    path('', include(router.urls))
]
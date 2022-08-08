from djoser import views as djoserviews
from rest_framework_nested import routers
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from djoser.urls import urlpatterns as url
from rest_framework_simplejwt import views as jwtviews

app_name = 'user'
router = routers.DefaultRouter()
router.register("", djoserviews.UserViewSet)

urlpatterns = [
   path('me/add-following/', views.Following.as_view(), name='following'),
   path('<int:pk>/', views.UserProfile.as_view(), name='profile'),
   path('<int:pk>/followers/', views.getFollowers.as_view(), name='followers'),
   path('<int:pk>/following/', views.getFollowing.as_view(), name='following'),
   path('', include(router.urls)),
   path("get-token", jwtviews.TokenObtainPairView.as_view(), name="jwt-create"),
   path("refresh-token", jwtviews.TokenRefreshView.as_view(), name="jwt-refresh"),
   path("verify-token", jwtviews.TokenVerifyView.as_view(), name="jwt-verify")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
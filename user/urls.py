from djoser import views
from rest_framework_nested import routers
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from djoser.urls import urlpatterns as url
app_name = 'user'

router = routers.DefaultRouter()

urlpatterns = [
   path('me/add-following/', views.Following.as_view(), name='following'),
   path('<int:pk>/', views.UserProfile.as_view(), name='profile'),
   path('<int:pk>/followers/', views.getFollowers.as_view(), name='followers'),
   path('<int:pk>/following/', views.getFollowing.as_view(), name='following'),
   router.register("", views.UserViewSet),
   path('', include('djoser.urls.jwt'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
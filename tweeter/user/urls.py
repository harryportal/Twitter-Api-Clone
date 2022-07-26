from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from djoser.urls import urlpatterns as url
app_name = 'user'


urlpatterns = [
    path('me/following/', views.following, name='following'),
    path('<int:pk>/followers', views.getFollowers.as_view(), name='followers'),
    path('<int:pk>/following', views.getFollowing.as_view(), name='following'),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from model_bakery import baker
from tweeter_api.models import Tweet
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestComment:
    @pytest.mark.skip
    def test_comment_on_tweet_authorised(self, authenticate_user, api_client):
        user = authenticate_user()
        tweet = baker.make(Tweet)
        response = api_client.post(f'/api/v1/comments/{tweet.id}/',{'content':'This is a random comment'})
        assert response.status_code == status.HTTP_200_OK

    def test_comment_on_tweet_anonymous(self, api_client):
        tweet = baker.make(Tweet)
        response = api_client.get(f'/api/v1/comments/{tweet.id}/',{'content':'This is a random comment'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_invalid_comment_on_tweet(self, authenticate_user, api_client):
        authenticate_user()
        tweet = baker.make(Tweet)
        response = api_client.post(f'/api/v1/comments/{tweet.id}/',{'content':''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
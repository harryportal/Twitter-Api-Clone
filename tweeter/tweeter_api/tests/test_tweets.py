import pytest
from rest_framework import status
from model_bakery import baker
from tweeter_api.models import Tweet


@pytest.mark.django_db
class TestCreateTweet:
    @pytest.mark.skip
    def test_create_tweet_user_authenticated_200(self, tweet, authenticate_user):
        authenticate_user()
        response = tweet({'content':'This is a new post'})
        assert response.status_code == status.HTTP_200_OK

    def test_create_tweet_user_anonymous(self, tweet):
        response = tweet({'title': 'This is a new post'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_create_tweet_invalid_data(self, tweet,authenticate_user):
        authenticate_user()
        response = tweet({'content': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
class TestRetrieveTweet:
    def test_get_tweet_anonymous_user(self,get_tweet):
        tweet = baker.make(Tweet)
        response = get_tweet(tweet.id)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_get_tweet_authorised_user(self, get_tweet, authenticate_user):
        authenticate_user()
        tweet = baker.make(Tweet)
        response = get_tweet(tweet.id)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == tweet.id

    def test_get_invalid_tweet_404(self,get_tweet, authenticate_user):
        authenticate_user()
        response = get_tweet('-1') # since a tweet id must always be positive
        assert response.status_code == status.HTTP_404_NOT_FOUND

@pytest.mark.django_db
class TestLikeTweet:
    @pytest.mark.skip
    def test_like_tweet_200(self,api_client, authenticate_user):
        authenticate_user()
        tweet = baker.make(Tweet)
        response = api_client.post(f'/api/v1/tweets/{tweet.id}/likes/')
        assert response.status_code == status.HTTP_200_OK
        assert tweet.likes.count() == 1

    def test_get_tweet_likes(self, api_client, authenticate_user):
        authenticate_user()
        tweet = baker.make(Tweet)
        response = api_client.get(f'/api/v1/tweets/{tweet.id}/likes/')
        assert response.status_code == status.HTTP_200_OK













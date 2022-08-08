import pytest

@pytest.fixture
def tweet(api_client):
    def create_tweet(tweet):
        return api_client.post('/api/v1/tweets/me/', tweet)
    return create_tweet

@pytest.fixture
def get_tweet(api_client):
    def tweet(id):
        return api_client.get(f'/api/v1/tweets/{id}/')
    return tweet
from rest_framework.test import APIClient
import pytest
from user.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticate_user(api_client):
    def authenticate():
        api_client.force_authenticate(user=User())
    return authenticate

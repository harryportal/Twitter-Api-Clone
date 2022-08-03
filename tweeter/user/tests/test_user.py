from rest_framework import status
import pytest
from model_bakery import baker
from user.models import User


@pytest.mark.django_db
class TestUser:
    def test_get_user_200(self, api_client, authenticate_user):
        authenticate_user()
        user = baker.make(User)  # create a user with model baker
        response = api_client.get(f'/api/v1/users/{user.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] > 0


    def test_get_user_anonymous_401(self, api_client, authenticate_user):
        user = baker.make(User)  # create a user with model baker
        response = api_client.get(f'/api/v1/users/{user.id}/')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED



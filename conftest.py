import pytest
from api.user_client import UserClient
from api.order_client import OrderClient
from helpers.generator import generate_user_data


@pytest.fixture
def user_client():

    return UserClient()


@pytest.fixture
def order_client():

    return OrderClient()


@pytest.fixture
def unique_user_data():

    return generate_user_data()


@pytest.fixture
def created_user(user_client):

    user_payload = generate_user_data()
    response = user_client.register_user(user_payload)
    
    token = response.json().get("accessToken")
    yield user_payload, token
    
    if token:
        user_client.delete_user(token)

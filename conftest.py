import pytest

from main.tests.factories import UserFactory


@pytest.fixture
def user_credentials():
    user = UserFactory.create()
    password = 'test_password'
    user.set_password(password)
    user.save()
    return user, password


@pytest.fixture
def authenticated_client(client, user_credentials):
    user, password = user_credentials
    client.login(username=user.username, password=password)
    return client

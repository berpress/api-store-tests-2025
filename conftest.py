import logging

import pytest

from api_client.client import StoreClient
from api_client.models.register import RegisterModel

logger = logging.getLogger("api_tests")


def pytest_addoption(parser):
    parser.addoption("--api-url", action="store", default="http://localhost:56733",
                     help="foo: bar or baz")

@pytest.fixture(scope="session")
def api_client(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start app on address {url}")
    client = StoreClient(url=url)
    return client

@pytest.fixture
def register_user(api_client) -> dict:
    body = RegisterModel().random()
    response_register = api_client.register(body=body)
    assert response_register.status_code == 201
    return body

@pytest.fixture
def auth_user(api_client):
    # register
    body = RegisterModel().random()
    response_register = api_client.register(body=body)
    assert response_register.status_code == 201, f"Check register request, status code is {response_register.status_code}"
    user_id = response_register.json()["uuid"]
    # auth
    response_auth = api_client.auth(body=body)
    assert response_auth.status_code == 200, "Check auth request"
    assert response_auth.json()['access_token'], "Check response"

    token = response_auth.json()['access_token']
    headers = {"Authorization": f"JWT {token}"}
    return headers, user_id
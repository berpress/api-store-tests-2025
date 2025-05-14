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
def register_new_user(api_client) -> dict:
    body = RegisterModel().random()
    response = api_client.register(body=body)
    assert response.status_code == 201, f"Check register request, status code is {response.status_code}"
    return body

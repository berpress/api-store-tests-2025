import logging

import pytest

from api_client.client import StoreClient

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
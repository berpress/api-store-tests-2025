import logging

import requests
from requests import Response

from utils.logs import log_response

logger = logging.getLogger("api_tests")


class StoreClient:
    def __init__(self, url: str):
        self.url = url
        self.requests = requests

    _REGISTER = "/register"
    _AUTH = "/auth"

    def register(self, body: dict) -> Response:
        res = self.requests.post(url=f"{self.url}{self._REGISTER}", json=body)
        log_response(response=res, request_body=body)
        return res

    def auth(self, body: dict) -> Response:
        res = self.requests.post(url=f"{self.url}{self._AUTH}", json=body)
        log_response(response=res, request_body=body)
        return res
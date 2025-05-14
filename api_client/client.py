import logging

import requests
from requests import Response

from utils.logger_api import log_response

logger = logging.getLogger("api_tests")


class StoreClient:
    def __init__(self, url: str):
        self.url = url
        self.requests = requests

    _REGISTER = "/register"
    _AUTH = "/auth"
    _ADD_USER = "/user_info/{}"

    def register(self, body: dict) -> Response:
        res = self.requests.post(url=f"{self.url}{self._REGISTER}", json=body)
        log_response(response=res, request_body=body)
        return res

    def auth(self, body: dict) -> Response:
        res = self.requests.post(url=f"{self.url}{self._AUTH}", json=body)
        log_response(response=res, request_body=body)
        return res

    def add_user_id(self, body: dict, user_id: int, headers: dict) -> Response:
        res = self.requests.post(url=f"{self.url}{self._ADD_USER.format(user_id)}", json=body, headers=headers)
        log_response(response=res, request_body=body)
        return res
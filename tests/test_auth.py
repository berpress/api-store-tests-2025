from api_client.models.register import RegisterModel
from api_client.texts.error_texts import ResponseErrorText


class TestAuth:
    def test_auth_new_user_2(self, api_client):
        """
        1. Register new user
        2. Try to auth user grom step 1
        3. Check status code is 200
        4. Check response
        """
        # register
        body = RegisterModel().random()
        response_register = api_client.register(body=body)
        assert response_register.status_code == 201, f"Check register request, status code is {response_register.status_code}"
        # auth
        response = api_client.auth(body=body)
        assert response.status_code == 200, "Check auth request"
        assert response.json()['access_token'] , "Check response"

    def test_auth_new_user(self, api_client, register_user):
        """
        1. Register new user
        2. Try to auth user grom step 1
        3. Check status code is 200
        4. Check response
        """
        # auth
        response = api_client.auth(body=register_user)
        assert response.status_code == 200, "Check auth request"
        assert response.json()['access_token'] , "Check response"

    def test_auth_new_user_empty_username(self, api_client):
        """
        1. Register new user with empty username
        2. Try to auth user grom step 1
        3. Check status code is 401
        4. Check response
        """
        # auth
        body = RegisterModel().random()
        body['username'] = None
        response = api_client.auth(body=body)
        assert response.status_code == 401, "Check auth request"
        assert response.json()["description"] == ResponseErrorText.INVALID_CREDENTIALS
        assert response.json()["error"] == ResponseErrorText.BAD_REQUEST


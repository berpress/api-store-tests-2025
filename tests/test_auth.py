from api_client.models.register import RegisterModel
from api_client.texts.response_error import ResponseError
from api_client.texts.response_text import ResponseText


class TestAuth:
    def test_auth_new_user_2(self, api_client):
        """
        1. Try to auth new user
        2. Check status code is 201
        3. Check response
        """
        body = RegisterModel().random()
        response = api_client.register(body=body)
        assert response.status_code == 201, f"Check register request, status code is {response.status_code}"

        response_auth = api_client.auth(body=body)
        assert response_auth.status_code == 200, f"Check register request, status code is {response.status_code}"

    def test_auth_new_user(self, api_client, register_new_user):
        """
        1. Try to auth new user
        2. Check status code is 201
        3. Check response
        """
        response = api_client.auth(body=register_new_user)
        assert response.status_code == 200, f"Check register request, status code is {response_auth.status_code}"

    # def test_register_new_user_with_empty_username_2(self, api_client):
    #     """
    #     1. Try to register new user with empty username
    #     2. Check status code is 400
    #     3. Check response
    #     """
    #     body = RegisterModel().random()
    #     body['username'] = None
    #     response = api_client.register(body=body)
    #     assert response.status_code == 400, f"Check register request, status code is {response.status_code}"
    #     assert response.json()['message'] == ResponseError.PASSWORD_USERNAME
    #
    # def test_register_new_user_with_empty_password_2(self, api_client):
    #     """
    #     1. Try to register new user with empty password
    #     2. Check status code is 400
    #     3. Check response
    #     """
    #     body = RegisterModel().random()
    #     body['password'] = None
    #     response = api_client.register(body=body)
    #     assert response.status_code == 400, f"Check register request, status code is {response.status_code}"
    #     assert response.json()['message'] == ResponseError.PASSWORD_USERNAME
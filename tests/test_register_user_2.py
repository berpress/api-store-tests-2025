from api_client.models.register import RegisterModel
from api_client.texts.error_texts import ResponseErrorText


class TestRegisterNewUser2:
    def test_register_new_user_2(self, api_client):
        """
        1. Try to register new user
        2. Check status code is 201
        3. Check response
        """
        body = RegisterModel().random()
        response = api_client.register(body=body)
        assert response.status_code == 201, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] is not None
        assert response.json()['uuid'] is not None
        assert response.json()['message'] == "User created successfully."

    def test_register_new_user_with_empty_username_2(self, api_client):
        """
        1. Try to register new user with empty username
        2. Check status code is 400
        3. Check response
        """
        body = RegisterModel().random()
        body['username'] = None
        response = api_client.register(body=body)
        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] == ResponseErrorText.USERNAME_PASSWORD

    def test_register_new_user_with_empty_password_2(self, api_client):
        """
        1. Try to register new user with empty password
        2. Check status code is 400
        3. Check response
        """
        body = RegisterModel().random()
        body['password'] = None
        response = api_client.register(body=body)
        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] == ResponseErrorText.USERNAME_PASSWORD
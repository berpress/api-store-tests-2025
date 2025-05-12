from api_client.models.register import RegisterModel


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
        assert isinstance(response.json()['message'], str)
        assert isinstance(response.json()['uuid'], int)

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
        assert response.json()['message'] == "Username and password are required fields"

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
        assert response.json()['message'] == "Username and password are required fields"
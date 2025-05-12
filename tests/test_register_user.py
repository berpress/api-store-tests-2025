import requests
from faker import Faker

URL = "http://localhost:56733"
fake = Faker()


class TestRegisterNewUser:
    def test_register_new_user(self):
        """
        1. Try to register new user
        2. Check status code is 201
        3. Check response
        """
        body = {"username": fake.email(), "password": "Password"}
        response = requests.post(url=f"{URL}/register", json=body)
        assert response.status_code == 201, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] is not None
        assert response.json()['uuid'] is not None
        assert response.json()['message'] == "User created successfully."
        assert isinstance(response.json()['message'], str)
        assert isinstance(response.json()['uuid'], int)

    def test_register_new_user_with_empty_username(self):
        """
        1. Try to register new user with empty username
        2. Check status code is 400
        3. Check response
        """
        body = {"username": None, "password": "Password"}
        response = requests.post(url=f"{URL}/register", json=body)
        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] == "Username and password are required fields"

    def test_register_new_user_with_empty_password(self):
        """
        1. Try to register new user with empty password
        2. Check status code is 400
        3. Check response
        """
        body = {"username": fake.email(), "password": None}
        response = requests.post(url=f"{URL}/register", json=body)
        assert response.status_code == 400, f"Check register request, status code is {response.status_code}"
        assert response.json()['message'] == "Username and password are required fields"
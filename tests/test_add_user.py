from api_client.models.add_user import AddUserModel
from api_client.models.register import RegisterModel
from api_client.texts.response_texts import ResponseTest


class TestAuth:
    def test_add_user(self, api_client):
        """
        1. Register new user
        2. Auth user from step 1
        3. Try to add user
        4. Check status code is 200
        5. Check response
        """
        # register
        body = RegisterModel().random()
        response_register = api_client.register(body=body)
        assert response_register.status_code == 201, f"Check register request, status code is {response_register.status_code}"
        user_id = response_register.json()["uuid"]
        # auth
        response_auth = api_client.auth(body=body)
        assert response_auth.status_code == 200, "Check auth request"
        assert response_auth.json()['access_token'] , "Check response"
        # add new user
        token = response_auth.json()['access_token']
        headers = {"Authorization": f"JWT {token}"}
        body_user = AddUserModel().random()
        response = api_client.add_user_id(body=body_user, user_id=user_id, headers=headers)
        assert response.status_code == 200
        assert response.json()["message"] == ResponseTest.CREATE_USER

    def test_add_user_2(self, api_client, auth_user):
        """
        1. Register new user
        2. Auth user from step 1
        3. Try to add user
        4. Check status code is 200
        5. Check response
        """
        headers, user_id = auth_user
        body_user = AddUserModel().random()
        response = api_client.add_user_id(body=body_user, user_id=user_id, headers=headers)
        assert response.status_code == 200
        assert response.json()["message"] == ResponseTest.CREATE_USER
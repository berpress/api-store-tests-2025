from faker import Faker

fake = Faker()

class RegisterModel:
    def random(self):
        return {"username": fake.email(), "password": "Password"}
from faker import Faker

fake = Faker()

class AddUserModel:
    def random(self):
        return {
            "phone": fake.phone_number(),
            "email": fake.email(),
            "address": {
                "city": fake.city(),
                "street": "ул. Проспект победы",
                "home_number": "10"
            }
        }
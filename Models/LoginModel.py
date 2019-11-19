import bcrypt
import pymongo
from pymongo import MongoClient


class LoginModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def check_user(self, data):
        user = self.Users.find_one({"Username": data.username})
        print(user)
        if user:
            if bcrypt.checkpw(data.password.encode(), user["password"]):
                return user
            else:
                return False
        else:
            return False

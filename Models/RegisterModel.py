import pymongo
from pymongo import MongoClient

class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):

        id1 = self.Users.insert({"username": data.username, "name": data.name, "password": data.password,
                                "email": data.email})
        print("uid is", id1)

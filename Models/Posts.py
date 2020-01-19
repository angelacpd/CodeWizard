import bcrypt
import pymongo
import humanize
from pymongo import MongoClient


class Posts:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users
        self.Posts = self.db.posts

    def insert_post(self, data):
        inserted = self.Posts.insert({"username": data.username, "content": data.content, "data_added": datetime.datetime.now()})
        post = self.Posts.find_one({"_id": inserted})
        new_post = {}
        new_post["name"] = self.Users.find_one({"username": post["username"]})["name"]
        new_post["content"] = post["content"]
        return post

    def get_all_posts(self):
        all_posts = self.Posts.find().sort("date_added", -1)
        new_posts = []

        for post in all_posts:
            print(post)
            post["user"] = self.Users.find_one({"username": post["username"]})
            post["timestamp"] = humanize.naturaltime(datetime.datetime.now() - post["date_added"])
            new_posts.append(post)

        return new_posts

    def get_user_posts(self, user):
        all_posts = self.Posts.find({"username": user}).sort("date_added", -1)
        new_posts = []

        for post in all_posts:
            print(post)
            post["user"] = self.Users.find_one({"username": post["username"]})
            new_posts.append(post)

        return new_posts

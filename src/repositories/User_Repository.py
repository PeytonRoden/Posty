from src.models import db
from src.models import User

class User_Repository:

    def get_all_users(self):
        # TODO get all users from the DB
        return None

    def get_user_by_id(self, user_id):
        # TODO get a single user from the DB using the ID
        return None

    def create_user(self, title, director, rating):
        # TODO create a new User in the DB

        return None

    def search_users(self, title):
        # TODO get all Users matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None


# Singleton to be used in other modules
user_repository_singleton = User_Repository()

from src.models import db
from src.models import Post

class Post_Repository:

    def get_all_posts(self):
        # TODO get all posts from the DB
        return None

    def get_post_by_id(self, post_id):
        # TODO get a single user from the DB using the ID
        return None

    def create_post(self, title, director, rating):
        # TODO create a new User in the DB

        return None

    def search_posts(self, title):
        # TODO get all Users matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None


# Singleton to be used in other modules
post_repository_singleton = Post_Repository()

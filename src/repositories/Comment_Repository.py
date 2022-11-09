from src.models import db
from src.models import Comment

class Comment_Repository:

    def get_all_comments(self):
        # TODO get all comments from the DB
        return None

    def get_comment_by_id(self, comment_id):
        # TODO get a single comment from the DB using the ID
        return None

    def get_comments_by_post_id(self, post_id):
        # TODO get all comments on post using post_id
        return None

    def get_comments_by_user_id(self, user_id):
        # TODO get all comments from user using user_id
        return None

    def create_comment(self, title, director, rating):
        # TODO create a new User in the DB

        return None

    def search_comments(self, comment_text):
        # TODO get all comments matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None


# Singleton to be used in other modules
comment_repository_singleton = Comment_Repository()

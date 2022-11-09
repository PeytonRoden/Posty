from src.models.models import db
from src.models.models import Like_

class Like_Repository:

    def get_all_likes(self):
        # TODO get all likes from the DB
        return None

    def get_like_by_id(self, like_id):
        # TODO get a single like from the DB using the ID 
        return None

    def get_likes_by_user_id(self, user_id):
        # TODO get likes from the DB using th user_ID, all the likes by a user
        return None

    def get_likes_by_post_id(self, post_id):
        # TODO get likes from the DB using the post_ID, all the likes on a post
        return None

    def create_like(self, title, director, rating):
        # TODO create a new User in the DB

        return None


# Singleton to be used in other modules
like_repository_singleton = Like_Repository()
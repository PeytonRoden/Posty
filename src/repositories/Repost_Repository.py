from src.models import db
from src.models import Repost

class Repost_Repository:

    def get_all_reposts(self):
        # TODO get all reposts from the DB
        return None

    def get_repost_by_id(self, repost_id):
        # TODO get a single repost from the DB using the ID 
        return None

    def get_reposts_by_user_id(self, user_id):
        # TODO get reposts from the DB using th user_ID, all the repposts by a user
        return None

    def get_reposts_by_post_id(self, post_id):
        # TODO get reposts from the DB using the post_ID, all the reposts on a post
        return None

    def create_repost(self, title, director, rating):
        # TODO create a new repost in the DB

        return None


# Singleton to be used in other modules
repost_repository_singleton = Repost_Repository()
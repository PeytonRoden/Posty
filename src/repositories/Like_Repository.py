from src.models.models import db
from src.models.models import Like_


class Like_Repository:

    def get_all_likes(self):
        # TODO get all likes from the DB
        return Like_.query.all()

    def get_like_by_id(self, like_id):
        # TODO get a single like from the DB using the ID
        return Like_.query.get(like_id)

    def get_likes_by_user_id(self, user_id):
        # TODO get likes from the DB using th user_ID, all the likes by a user
        return Like_.query.get(user_id)

    def get_likes_by_post_id(self, post_id):
        # TODO get likes from the DB using the post_ID, all the likes on a post
        return Like_.query.get(post_id)

    def create_like(self, post_id, user_id):
        # TODO create a new User in the DB
        new_like = Like_(post_id=post_id, user_id=user_id)
        db.session.add(new_like)
        db.session.commit()

        return new_like


# Singleton to be used in other modules
like_repository_singleton = Like_Repository()

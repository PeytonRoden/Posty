from src.models.models import db
from src.models.models import Comment

class Comment_Repository:

    def get_all_comments(self):
        # TODO get all comments from the DB
        return None

    def get_comment_by_id(self, comment_id):
        # TODO get a single comment from the DB using the ID
        comment = Comment.query.get(comment_id)

        return comment

    def get_comments_by_post_id(self, post_id):
        # TODO get all comments on post using post_id
        return None

    def get_comments_by_user_id(self, user_id):
        # TODO get all comments from user using user_id
        return None

    def create_parent_comment(self, comment_text, post_id, user_id):
        # TODO create a new parent comment in the DB

        new_comment = Comment(comment_text = comment_text, post_id= post_id, user_id = user_id)
        db.session.add(new_comment)
        db.session.commit()

        return new_comment

    def create_child_comment(self, comment_text, post_id, user_id, parent_comment_id):
        # TODO create a new child comment in the DB

        new_comment = Comment(comment_text = comment_text, post_id= post_id, user_id = user_id, parent_comment_id = parent_comment_id)
        db.session.add(new_comment)
        db.session.commit()

        return None

    def search_comments(self, comment_text):
        # TODO get all comments matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None


# Singleton to be used in other modules
comment_repository_singleton = Comment_Repository()

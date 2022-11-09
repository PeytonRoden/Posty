from src.models.models import db
from src.models.models import Post

class Post_Repository:

    def get_all_posts(self):
        # TODO get all posts from the DB
        return Post.query.all()

    def get_post_by_id(self, post_id):
        # TODO get a single user from the DB using the ID
        return Post.query.get(post_id)

    def create_post(self, university, post_title, post_text, user_id):

        new_post = Post(university = university, post_title = post_title, post_text = post_text, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()
        
        return None

    def search_posts(self, title):
        # TODO get all Users matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None


# Singleton to be used in other modules
post_repository_singleton = Post_Repository()

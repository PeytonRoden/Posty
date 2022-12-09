from src.models.models import db
from src.models.models import User_

class User_Repository:

    def get_all_users(self):
        # TODO get all users from the DB
        return User_.query.all()

    def get_user_by_id(self, user_id):
        # TODO get a single user from the DB using the ID
        user = User_.query.get(user_id)
        return user

    def create_user(self, first_name, last_name, username, email, user_password, university):
        # TODO create a new User in the DB

        new_user = User_(first_name = first_name, last_name = last_name, username = username, email = email, user_password = user_password, university=university)
        db.session.add(new_user)
        db.session.commit()

        return None

    def get_user_by_username(self, username):
        return User_.query.filter_by(username = username).first()

    def search_users(self, title):
        # TODO get all Users matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        return None

    def set_profile_pic(self, user_id, profile_pic_url):
        user = self.get_user_by_id(user_id)
        user.avatar_url = profile_pic_url
        db.session.commit()



# Singleton to be used in other modules
user_repository_singleton = User_Repository()

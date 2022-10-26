from src.models.User import User

_user_repo = None


def get_user_repository():
    global _user_repo

    class User_repo:
        """In memory database which is a simple list of Users"""

        def __init__(self) -> None:
            self._db: list[User] = []

        def get_all_users(self) -> list[User]:
            """Simply return all users from the in-memory database"""
            return self._db

        def get_user_by_name(self, name: str) -> User | None:
            """Get a single movie by its title or None if it does not exist"""
            # Perform a linear search through the in-memory database
            for user in self._db:
                # If user matches names return user
                if user.name == name:
                    return user
            # If we made it this far, no users matched so return None
            return None


        def get_user_by_email(self, email: str) -> User | None:
            """Get a single movie by its title or None if it does not exist"""
            # Perform a linear search through the in-memory database
            for user in self._db:
                # If user matches names return user
                if user.email == email:
                    return user
            # If we made it this far, no users matched so return None
            return None

        def create_user(self, name: str, email: str, password: str, university: str) -> User:
            """Create a new user and return it"""
            # Create the user instance
            user = User(name, email, password, university)
            # Save the instance in our in-memory database
            self._db.append(user)
            # Return the user instance
            return user

    # Singleton to be used in other modules
    if _user_repo is None:
        _user_repo = User_repo()

    return _user_repo

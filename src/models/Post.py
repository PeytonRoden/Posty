from src.models.User import User


class Post:
    """Holds, name, email, password, and university name"""
    """Add maybe a list of post IDs and comment ids"""

    def __init__(self, user: User, university: str, post_title: str, post: str) -> None:
        self.user = user
        self.university = university
        self.post_title = post_title
        self.post = post

from src.models.Post import Post
from src.models.User import User
_post_repo = None


def get_post_repository():
    global _post_repo

    class Post_repo:
        """In memory database which is a simple list of Posts"""

        def __init__(self) -> None:
            self._db: list[Post] = []

        def get_all_posts(self) -> list[Post]:
            """Simply return all posts from the in-memory database"""
            return self._db

        def get_post_by_title(self, title: str) -> Post | None:
            """Get a single post by its title or None if it does not exist"""
            posts = []

            # Perform a linear search through the in-memory database
            for post in self._db:
                # If title matches in db return it
                if post.title == title:
                    posts.append(post)

            if(len(posts) != 0):
                return posts


            # If we made it this far, no posts matched so return None
            return None


        def create_post(self, user: User, university: str, post_title: str, post: str) -> User:
            """Create a new post and return it"""
            # Create the post instance
            post = Post(user, university, post_title, post)
            # Save the instance in our in-memory database
            self._db.append(post)
            # Return the user instance
            return post

    # Singleton to be used in other modules
    if _post_repo is None:
        _post_repo = Post_repo()

    return _post_repo

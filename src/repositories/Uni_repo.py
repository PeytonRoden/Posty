from src.models.Uni import Uni

def get_uni_repository():
    global _uni_repo

    class Uni_repo:
        """In memory database which is a simple list of Users"""

        def __init__(self) -> None:
            self._db: list[Uni] = []

        def get_all_uni(self) -> list[Uni]:
            """Simply return all users from the in-memory database"""
            return self._db

        def get_uni_by_name(self, name: str) -> Uni | None:
            """Get a single movie by its title or None if it does not exist"""
            # Perform a linear search through the in-memory database
            for uni in self._db:
                # If user matches names return user
                if uni.name == name:
                    return uni
            # If we made it this far, no users matched so return None
            return None


        def create_uni(self, name: str, logo: str, subpage: str) -> Uni:
            """Create a new user and return it"""
            # Create the user instance
            uni = Uni(name, logo, subpage)
            # Save the instance in our in-memory database
            self._db.append(uni)
            # Return the user instance
            return uni

    # Singleton to be used in other modules
    if _uni_repo is None:
        _uni_repo = Uni_repo()

    return _uni_repo

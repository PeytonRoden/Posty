class User:
    """Holds, name, email, password, and university name"""
    """Add maybe a list of post IDs and comment ids"""

    def __init__(self, name: str, email: str, password: str, university: str) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.university = university


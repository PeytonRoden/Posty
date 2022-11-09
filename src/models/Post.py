from src.models.User import User
from src.models.Comment_Tree import Comment_Tree


class Post:
    """Holds, name, email, password, and university name"""
    """Add maybe a list of post IDs and comment ids"""

    def __init__(self, postID: str, user: User, university: str, post_title: str, post: str) -> None:
        self.user = user
        self.university = university
        self.post_title = post_title
        self.post = post
        self.postID = postID
        self.__addCommentTree()

    def __addCommentTree(self)->None:
        self.comment_tree = Comment_Tree()

    def addBaseComment(self, comment):
        self.comment_tree.add_base_comment(comment)

    def getCommentTree(self) -> Comment_Tree:
        return self.comment_tree


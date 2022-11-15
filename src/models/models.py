from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User_(db.Model):

    #serial field that automatically increments
    user_id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
    username = db.Column(db.String(255), nullable = False, unique = True)
    email = db.Column(db.String(255), nullable = False, unique = True)
    user_password = db.Column(db.String(255), nullable = False)
    university = db.Column(db.String(255), nullable = False)
    account_created = db.Column(db.DateTime, default=db.func.current_timestamp())


    admin_ = db.Column(db.Boolean, default = False, nullable = False)



class Post(db.Model):

    #serial field that automatically increments
    post_id = db.Column(db.Integer, primary_key=True)

    university = db.Column(db.String(255), nullable = False)
    post_title = db.Column(db.String(255), nullable = False)
    post_text = db.Column(db.String(255), nullable = False)
    post_datetime = db.Column(db.DateTime, default=db.func.current_timestamp())

    number_likes = db.Column(db.Integer, nullable = False, default = 0 )
    number_comments = db.Column(db.Integer, nullable = False, default = 0 )
    number_reposts = db.Column(db.Integer, nullable = False, default = 0 )

    user_id = db.Column(db.Integer, db.ForeignKey(User_.user_id), nullable=False)
    user = db.relationship('User_', backref='posts', lazy=False, primaryjoin="User_.user_id == Post.user_id")




class Comment(db.Model):

    #serial field that automatically increments
    comment_id = db.Column(db.Integer, primary_key=True)
    
    comment_text = db.Column(db.String(255), nullable = False)
    comment_datetime = db.Column(db.DateTime, default=db.func.current_timestamp())
    parent_comment_id = db.Column(db.Integer, nullable = True)


    post_id = db.Column(db.Integer, db.ForeignKey(Post.post_id), nullable=False)
    post = db.relationship('Post', backref='post_comments', lazy=True, primaryjoin="Comment.post_id == Post.post_id")
    user_id = db.Column(db.Integer, db.ForeignKey(User_.user_id), nullable=False)
    user = db.relationship('User_', backref='commenter', lazy=True, primaryjoin="User_.user_id == Comment.user_id")



class Like_(db.Model):
    
    #serial field that automatically increments
    like_id = db.Column(db.Integer, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey(Post.post_id), nullable=False)
    post = db.relationship('Post', backref='post_likes', lazy=True , primaryjoin="Post.post_id == Like_.post_id")
    user_id = db.Column(db.Integer, db.ForeignKey(User_.user_id), nullable=False)
    user = db.relationship('User_', backref='user_likes', lazy=True, primaryjoin="User_.user_id == Like_.user_id")




class Repost(db.Model):

    #serial field that automatically increments
    repost_id = db.Column(db.Integer, primary_key=True)
    
    reposter_user_id = db.Column(db.Integer, db.ForeignKey(User_.user_id), nullable=False)
    reposter_user = db.relationship('User_', backref='user_reposts', lazy=True, primaryjoin="User_.user_id == Repost.reposter_user_id")

    post_id = db.Column(db.Integer, db.ForeignKey(Post.post_id), nullable=False)
    post = db.relationship('Post', backref='post_reposts', lazy=True, primaryjoin="Post.post_id == Repost.post_id")

    poster_user_id = db.Column(db.Integer, db.ForeignKey(User_.user_id), nullable=False)
    poster_user = db.relationship('User_', backref='og_posters', lazy=True, primaryjoin="User_.user_id == Repost.poster_user_id")
    


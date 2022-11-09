from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.model):

    #serial field that automatically increments
    user_id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)
    username = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255), nullable = False)
    user_password = db.Column(db.String(255), nullable = False)
    university = db.Column(db.String(255), nullable = False)


    admin = db.Column(db.Boolean, default = False, nullable = False)



class Post(db.Model):

    #serial field that automatically increments
    post_id = db.Column(db.Integer, primary_key=True)

    university = db.Column(db.String(255), nullable = False)
    post_title = db.Column(db.String(255), nullable = False)
    post_text = db.Column(db.String(255), nullable = False)
    post_datetime = db.column(db.DateTime, nullable = False)

    number_likes = db.Column(db.Integer, nullable = False)
    number_comments = db.Column(db.Integer, nullable = False)
    number_reposts = db.Column(db.Integer, nullable = False)

    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    user = db.relationship('User', backref='posts', lazy=True)




class Comment(db.Model):

    #serial field that automatically increments
    comment_id = db.Column(db.Integer, primary_key=True)
    
    comment_text = db.Column(db.String(255), nullable = False)
    comment_datetime = db.column(db.DateTime, nullable = False)
    parent_comment_id = db.Column(db.Integer, nullable = True)


    post_id = db.Column(db.Integer, db.ForeignKey('Post.post_id'), nullable=False)
    post = db.relationship('Post', backref='post_comments', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    user = db.relationship('User', backref='user_comments', lazy=True)



class Like_(db.Model):
    
    #serial field that automatically increments
    like_id = db.Column(db.Integer, primary_key=True)

    post_id = db.Column(db.Integer, db.ForeignKey('Post.post_id'), nullable=False)
    post = db.relationship('Post', backref='post_likes', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    user = db.relationship('User', backref='user_likes', lazy=True)




class Repost(db.Model):

    #serial field that automatically increments
    repost_id = db.Column(db.Integer, primary_key=True)
    
    reposter_user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    reposter_user = db.relationship('User', backref='user_reposts', lazy=True)

    post_id = db.Column(db.Integer, db.ForeignKey('Post.post_id'), nullable=False)
    post = db.relationship('Post', backref='post_reposts', lazy=True)

    poster_user_id = db.Column(db.Integer, db.ForeignKey('User.user_id'), nullable=False)
    poster_user = db.relationship('User', backref='og_posters', lazy=True)
    


from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required, logout_user


from src.repositories.Post_Repository import post_repository_singleton
from src.repositories.User_Repository import user_repository_singleton
from src.repositories.Comment_Repository import comment_repository_singleton
from src.repositories.Like_Repository import like_repository_singleton
from src.models.models import Post
from src.models.models import User_

from src.models.models import db

app = Flask(__name__) # __name__ refers to the module name
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/posty_database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



global post_list
post_list = post_repository_singleton.get_all_posts()

#login stuff
"""
global logged_in 
logged_in = False
global current_user
current_user = None
"""

#new loggin stuff
from flask_login import LoginManager
from flask_login import current_user
login_manager = LoginManager()
login_manager.init_app(app)




@app.route('/') # Python decorator, new syntax
def index():
    post_list = post_repository_singleton.get_all_posts()
    return render_template("index.html", current_user = current_user, post_list= post_list)

@app.route('/index') # Python decorator, new syntax
def go_to_index():
    post_list = post_repository_singleton.get_all_posts()
    return render_template("index.html", current_user = current_user, post_list= post_list)

@app.route('/login_page') # Python decorator, new syntax
def login_page():
    return render_template("login_page.html", current_user = current_user)

@app.route('/home_page') # Python decorator, new syntax
def home_page():
    post_list = post_repository_singleton.get_all_posts()
    return render_template("index.html", current_user = current_user, post_list= post_list)

@app.route('/sign_up_page') # Python decorator, new syntax
def sign_up_page():
    return render_template("sign_up_page.html", current_user = current_user)

@app.route('/account_info_page') # Python decorator, new syntax
def account_info_page():
    return render_template("account_info.html", current_user = current_user)


@app.route('/create_new_post_page') # Python decorator, new syntax
def create_new_post_page():

    if(current_user == None):
        #need to be logged in to make posts
        return index()

    return render_template("create_new_post.html", current_user = current_user)



"""
@app.post('/sign_up')  # Python decorator, new syntax
def sign_up():

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    username = request.form.get('username')
    user_university = request.form.get('university')
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    user_repeat_password = request.form.get('repeat_password')

    if (user_password != user_repeat_password):
        # TODO: handle this
        flash('Password Does Not Match')
        return redirect("/sign_up_page")

    user_repository_singleton.create_user(
        firstname, lastname, username, user_email, user_password, user_university)

    flash('Form Submitted Successfully')

    return redirect("/login_page")
"""

@app.post('/sign_up')  # Python decorator, new syntax
def sign_up():
    # code to validate and add user to database goes here
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    username = request.form.get('username')
    user_university = request.form.get('university')
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    user_repeat_password = request.form.get('repeat_password')

    #if passwords don't match redirect
    if (user_password != user_repeat_password):
        # TODO: handle this
        flash('Password Does Not Match')
        return sign_up_page()

    user = User_.query.filter_by(email=user_email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return sign_up_page()


    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    user_repository_singleton.create_user(firstname, lastname, username, user_email, generate_password_hash(user_password, method='sha256'), user_university)

    flash('Form Submitted Successfully')

    return login_page()


"""
@login_manager.user_loader
def user_loader(user_id):
    ///Given *user_id*, return the associated User object.
    ///
    ///:param unicode user_id: user_id (email) user to retrieve
    ///
    ///
    return User_.query.get(user_id)
"""

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User_.query.get(int(user_id))



@app.post('/login') # Python decorator, new syntax
def login():
    # login code goes here
    username = request.form.get('username')
    password = request.form.get('password')

    user = User_.query.filter_by(username=username).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.user_password, password):
        flash('Please check your login details and try again.')
        #if password details don't match reload the page
        return login_page()

    # if the above check passes, then we know the user has the right credentials
    login_user(user)

    print("logged in :"+ current_user.username)

    # if the above check passes, then we know the user has the right credentials
    return index()


@app.post('/logout')
@login_required
def logout():
    logout_user()
    return index()


"""
@app.post('/login') # Python decorator, new syntax
def login():
    global logged_in
    global current_user


    username = request.form.get('username')
    user_password = request.form.get('password')


    user = user_repository_singleton.get_user_by_username(username)

    if(user == None):
        #user doesn't exist
        print("user  === none")
        return redirect("/login_page")

    if(user.user_password != user_password):
        #passwords don't match
        print("passwrods don't match")
        return redirect("/login_page")

    if current_user == None:
        print("No current user")

    #at this point user exists and password matches
    logged_in = True
    current_user = user


    #go back to index, name and uni will appear at top of screen
    return redirect("/")
"""



@app.post('/create_new_post') # Python decorator, new syntax
@login_required
def create_new_post():
    global post_list

    title = request.form.get('title')
    post_text = request.form.get('post')

    if(current_user.is_authenticated):

        post_repository_singleton.create_post(current_user.university, title, post_text, current_user.user_id)
        #update post list
        post_list = post_repository_singleton.get_all_posts()



    return index()


"""
@app.post('/logout') # Python decorator, new syntax
def logout():
    global current_user

    current_user = None

    return redirect("/")
"""

@app.route('/post_viewer/<int:post_id>')
def post_viewer(post_id):
    global post_list

    selected_post_id = post_id

    #grabbing posts using post ids
    user_post = None
    
    for post in post_list:
        if(str(selected_post_id ) == str(post.post_id)):
            user_post = post

    user_post = post_repository_singleton.get_post_by_id(post_id)


    if(user_post == None):
        return index()



    #need to find list of all comments associated with this particular post and pass that into render tempate
    comments = post_repository_singleton.returnAllComments(selected_post_id )
    print(comments)


    #if the comments list is empty display the page
    if(len(comments) == 0):
        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {})



    #organize comments list into a dictionary where
    # {  parents comment: [child comment 1, child comment 2, child comment 3]   }

    comment_dictionary = generate_comment_dictionary(post_id)

    print(comment_dictionary)

    return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= False)


@app.route('/comment_text_area/<int:post_id>')
@login_required
def post_viewer_comment_text_area(post_id):

    #get post object using id
    user_post = post_repository_singleton.get_post_by_id(post_id)

    #get comment dictionary
    comment_dictionary = generate_comment_dictionary(post_id)

    #can't comment if not logged in
    if(not current_user.is_authenticated):
        #if the comments list is empty display the page
        if(len(comment_dictionary) == 0):
            return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {}, parent_comment=False)

        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= False)

    #if the comments list is empty display the page
    if(len(comment_dictionary) == 0):
        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {}, parent_comment=True)

    return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= True)
    

@app.route('/comment_text_area/comment/<int:post_id>')
@login_required
def post_viewer_comment(post_id):

    comment_dictionary = generate_comment_dictionary(post_id)
    user_post = post_repository_singleton.get_post_by_id(post_id)

    #can't comment if not logged in
    if(not current_user.is_authenticated):
        #if the comments list is empty display the page
        if(len(comment_dictionary) == 0):
            return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {}, parent_comment=False)

        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= False)


    comment_text = request.args.get('comment_text')

    comment_repository_singleton.create_parent_comment(comment_text, post_id , current_user.user_id)
    comment_dictionary = generate_comment_dictionary(post_id)

    #if the comments list is empty display the page
    if(len(comment_dictionary) == 0):
        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {}, parent_comment=False)

    return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= False)
    





@app.route('/comment_text_area/<int:post_id>/<int:comment_id>')
@login_required
def post_viewer_reply_to_comment(post_id, comment_id):

    #get post object using id
    user_post = post_repository_singleton.get_post_by_id(post_id)
    comment_to_reply = comment_repository_singleton.get_comment_by_id(comment_id)

    #get comment dictionary
    comment_dictionary = generate_comment_dictionary(post_id)

    #can't comment if not logged in
    if(not current_user.is_authenticated):
        #if the comments list is empty display the page
        if(len(comment_dictionary) == 0):
            return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {}, parent_comment=False)

        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= False)

    #if the comments list is empty display the page
    if(len(comment_dictionary) == 0):
        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {}, parent_comment=False)

    return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= False, comment_to_reply = comment_to_reply)
    


@app.route('/comment_text_area/comment/<int:post_id>/<int:comment_id>')
@login_required
def post_viewer_comment_to_comment(post_id, comment_id):

    comment_dictionary = generate_comment_dictionary(post_id)
    print(comment_dictionary)
    user_post = post_repository_singleton.get_post_by_id(post_id)
    comment_to_reply = comment_repository_singleton.get_comment_by_id(comment_id)


    #can't comment if not logged in
    if(not current_user.is_authenticated):
        #if the comments list is empty display the page
        if(len(comment_dictionary) == 0):
            return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {}, parent_comment=False)

        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= False)



    comment_text = request.args.get('comment_text')
    comment_repository_singleton.create_child_comment(comment_text, post_id , current_user.user_id, comment_id)
    comment_dictionary = generate_comment_dictionary(post_id)


    #if the comments list is empty display the page
    if(len(comment_dictionary) == 0):
        return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = {}, parent_comment=False)

    return render_template("post_viewer.html", current_user = current_user, post = user_post, comment_dictionary = comment_dictionary, parent_comment= False)
    




def generate_comment_dictionary(selected_post_id):

    
    #organize comments list into a dictionary where
    # {  parents comment: [child comment 1, child comment 2, child comment 3]   }

    comments = post_repository_singleton.returnAllComments(selected_post_id )

    comment_dictionary = {}

    #parent comments
    for comment in comments:
        if comment.parent_comment_id == None:
            comment_dictionary[comment] = []

    #child comments
    for comment in comments:
        if comment.parent_comment_id != None:

            try:
                comment_dictionary[comment_repository_singleton.get_comment_by_id(comment.parent_comment_id)].append(comment)
            except:
                print("hi")

    return comment_dictionary


@app.route('/delete_comment/<int:post_id>/<int:comment_id>')
@login_required
def delete_comment(comment_id,post_id):

    comment_repository_singleton.delete_comment(comment_id)

    return redirect(url_for('post_viewer', post_id = post_id))



@app.route('/delete_post_index/<int:post_id>')
@login_required
def delete_post_index(post_id):
    post_repository_singleton.delete_post(post_id)
    return redirect(url_for('go_to_index'))


@app.route('/delete_post_post_viewer/<int:post_id>')
@login_required
def delete_post_post_viewer(post_id):
    
    post_repository_singleton.delete_post(post_id)

    return redirect(url_for('go_to_index'))



@app.route('/like/<int:post_id>')
@login_required
def like(post_id):

    #creating like and incrementing number of likes on post
    like_created = like_repository_singleton.create_like(post_id, current_user.user_id )

    if(like_created):
        post_repository_singleton.increment_num_likes(post_id)
    else:
        post_repository_singleton.decrement_num_likes(post_id)

    return redirect(url_for('post_viewer', post_id = post_id))


@app.route('/index_like/<int:post_id>')
@login_required
def index_like(post_id):

    #creating like and incrementing number of likes on post
    like_created = like_repository_singleton.create_like(post_id, current_user.user_id )

    if(like_created):
        post_repository_singleton.increment_num_likes(post_id)
    else:
        post_repository_singleton.decrement_num_likes(post_id)


    return redirect(url_for('go_to_index'))
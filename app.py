from flask import Flask, render_template, request, url_for, redirect
from src.repositories.User_repo import get_user_repository

app = Flask(__name__) # __name__ refers to the module name


user_repo = get_user_repository()

#login stuff
global logged_in 
logged_in = False
global current_user
current_user = None


@app.route('/') # Python decorator, new syntax
def index():
    return render_template("index.html", current_user = current_user)

@app.route('/login_page') # Python decorator, new syntax
def login_page():
    return render_template("login_page.html")

@app.route('/home_page') # Python decorator, new syntax
def home_page():
    return render_template("index.html", current_user = current_user)

@app.route('/sign_up_page') # Python decorator, new syntax
def sign_up_page():
    return render_template("sign_up_page.html")


@app.post('/create_new_user') # Python decorator, new syntax
def create_new_user():

    user_name = request.form.get('name')
    user_university = request.form.get('university')
    user_email = request.form.get('email')
    user_password = request.form.get('password')
    user_repeat_password = request.form.get('repeat_password')

    if(user_password != user_repeat_password):
        #TODO: handle this
        return redirect("/sign_up_page")

    user_repo.create_user(user_name, user_email,user_password,user_university)

    print(user_repo.get_user_by_name(user_name).name)


    return redirect("/login_page")



@app.post('/login_page/login') # Python decorator, new syntax
def login():
    global logged_in
    global current_user


    user_email = request.form.get('email')
    user_password = request.form.get('password')


    user = user_repo.get_user_by_email(user_email)

    if(user == None):
        #user doesn't exist
        print("user  === none")
        return redirect("/login_page")

    if(user.password != user_password):
        #passwords don't match
        print("passwrods don't match")
        return redirect("/login_page")

    print(logged_in)
    if current_user == None:
        print("No current user")
    else:
        print(current_user.name)

    #at this point user exists and password matches
    logged_in = True
    current_user = user

    print(logged_in)
    print(current_user.name)

    return redirect("/")

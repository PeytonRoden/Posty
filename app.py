from flask import Flask, render_template, request, url_for, redirect
import random

app = Flask(__name__) # __name__ refers to the module name

names_and_events = {}

@app.route('/') # Python decorator, new syntax
def index():
    return render_template("index.html")

@app.route('/login_page') # Python decorator, new syntax
def login_page():
    return render_template("login_page.html")

@app.route('/home_page') # Python decorator, new syntax
def home_page():
    return render_template("index.html")

@app.route('/sign_up_page') # Python decorator, new syntax
def sign_up_page():
    return render_template("sign_up_page.html")


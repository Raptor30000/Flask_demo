"""Purpouse of this Blueprint is to mointain communication mainly in order to create accouts and login and logout user"""
import flask_login
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from .models import *
from flask_login import login_user, login_required, logout_user
from datetime import datetime

#Create a bluprint class and add authorization enpoitns to it to register it in flask application and in the login maganer
auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST'])
def signup_post():
    """Main purpouse of this enpoint is to allow users to create an account with
    email, name and password required """

    #Get email from request, if not present in request body, return alert
    if email := request.json.get('email'):
        pass
    else:
        return jsonify("Email is required!")
    # Get password from request, if not present in request body, return alert
    if password := request.json.get('password'):
        pass
    else:
        return jsonify("Password is required!")
    # Get name from request, if not present in request body, return alert
    if name := request.json.get('name'):
        pass
    else:
        return jsonify("Name is required!")

    #Search for user in the database based on email from the request
    user = User.query.filter_by(email=email).first()

    #If there is user registered in database on this email return with alert
    if user:
        return jsonify('Account with this email adress already exist!')

    #Create a User class object to be added as a record to the User table in the database. User class is class from the models
    new_user = User(name=name,
                    email=email,
                    password=generate_password_hash(password, method='pbkdf2:sha1:2000'),
                    created=datetime.now())

    #Add User class object to the session to add it as a record to the database
    db.session.add(new_user)
    #Commit session to commit adding new user
    db.session.commit()

    return jsonify("Signing up completed! Please Log in with you email and password")

@auth.route('/login', methods=['POST'])
def login_post():
    """main purpous of this function is allow users to log in by sending request with credentials.
    This function should not be use for oauth logins. Oauth will be maintain in separate function in future"""
    # Get email from request, if not present in request body, return alert
    if email := request.json.get('email'):
        pass
    else:
        return jsonify("Email is required!")

    # Get password from request, if not present in request body, return alert
    if password := request.json.get('password'):
        pass
    else:
        return jsonify("password is required!")

    #if user send in request element remember it should be saved in this variable and pass login_user funtion
    #It allows to remember user and its from default set as true in flask-login
    #but in future i want make sessions not persistent so i adding it
    remember = True if request.json.get('remember') else False

    #Search for user in the database by its email
    user = User.query.filter_by(email=email).first()

    #If login and passord dont match return with alert
    if not user or not check_password_hash(user.password, password):
        return jsonify("Invaild credentials")

    #log in user in Login_manager
    login_user(user, remember=remember)
    return jsonify("Login succesfull!")


@auth.route('/loggedUser', methods=['GET'])
@login_required
def login_get():
    """Main purpouse of this function is to return data of the logged in user to show it on the page"""

    #Check if user is logged in and if yes return its data,
    #if is redundant with decorator login_required but I didnt deleted it just in case
    if user := User.query.filter_by(id=flask_login.current_user.id).first():
        return jsonify(
            email=user.email,
            name=user.name,
            created=user.created,
            recipes=user.recipes
        )
    else:
        return jsonify("User not logged in!")


@auth.route('/logout')
@login_required
def logout():
    """Endpoint allowing logged user to log out"""
    logout_user()
    return jsonify('Logout successfull')


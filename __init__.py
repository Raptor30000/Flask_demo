#Purpouse of this file is to by run by by deployment infrastructure to start and configure the Flask application

from flask import Flask
from .database import db
from .models import User, Recipes, Timers, Ingredients



def create_app():
    """
    Purpouse of this function is to create Flask Application Object,
    configure the application by registering blueprints and database initial configs,
    initialize the login manager and set up authorization restrictions
    :return:
    Flask application instance,
    Database instance
    """

    #Create Flask instance, this will be used to run and configure apllication and its returned in this funtion return
    application = Flask(__name__)

    application.config['SECRET_KEY'] = 'secretly_secret'
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(application)

    with application.app_context():
        db.create_all()

    return application


app = create_app()


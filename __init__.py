#Purpouse of this file is to by run by by deployment infrastructure to start and configure the Flask application

from flask import Flask
def create_app():
    """
    Purpouse of this function is to create Flask Application Object,
    configure the application by registering blueprints and database initial configs,
    initialize the login manager and set up authorization restrictions
    :return:
    Flask application instance
    """

    #Create Flask instance, this will be used to run and configure apllication and its returned in this funtion return
    app = Flask(__name__)

    return app

app=create_app()
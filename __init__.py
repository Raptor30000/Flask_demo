#Purpouse of this file is to by run by by deployment infrastructure to start and configure the Flask application

from flask import Flask, jsonify
from .database import db
from .models import User
from flask_login import LoginManager


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

    #Secret key is safty feature, before pass this to production i rekomend change it.
    #Database URI define name of the database and its type, db will be created in ../instance/database.db
    application.config['SECRET_KEY'] = 'secretly_secret'
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    #Initalizing Login manager which will be responsible for managing logged users sessions
    login_manager = LoginManager()
    #Setting up where user will be redireted if tried to reach login_required enpoind while not beeing logged in
    #The shema is "blueprint_name.function_name"
    login_manager.login_view = 'main.test'
    #Bind login manager with the flask application
    login_manager.init_app(application)

    #Binding database with Flask application, required to both work with each other,
    #can be perform instead when initializing SQLAlchemy object,
    #but in this case application had to be passed to do this which will cause cirrcular import
    db.init_app(application)

    #This function binds user_id from login manager with record id in the table Users in the database
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #this will create tables in db if required,
    #note that whis will not change tables which was previously created if their models are changed,
    #note that all models have to be imported before this line
    with application.app_context():
        db.create_all()

    #Register blueprint for authorization specjalized enpoints
    from .api_v1.auth import auth_api
    application.register_blueprint(blueprint=auth_api)

    #Register blueprint for non access restricted endpoints
    from .api_v1.main import main_api
    application.register_blueprint(blueprint=main_api)

    #This function allow to specyfie response when unauthorized user trying to reach restricted endpoint
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return jsonify("This enpoint is only allowed for logged in users! Please log in or sign up"), 403

    return application


#creating the instance of Flask application
app = create_app()

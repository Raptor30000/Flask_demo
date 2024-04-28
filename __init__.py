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

    #Secret key is safty feature, before pass this to production i rekomend change it.
    #Database URI define name of the database and its type, db will be created in ../instance/database.db
    application.config['SECRET_KEY'] = 'secretly_secret'
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    #Binding database with Flask application, required to both work with each other,
    #can be perform instead when initializing SQLAlchemy object,
    #but in this case application had to be passed to do this which will cause cirrcular import
    db.init_app(application)

    #this will create tables in db if required,
    #note that whis will not change tables which was previously created if their models are changed,
    #note that all models have to be imported before this line
    with application.app_context():
        db.create_all()

    #importing main Blueprint object and registering it in app
    from .main import main
    application.register_blueprint(blueprint=main)

    return application


#creating the instance of Flask application
app = create_app()

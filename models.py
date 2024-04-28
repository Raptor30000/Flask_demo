"""Purpouse of this file is to definie tables and theirs structure to be imported to __init__
where database will be created if base on them and to be imported to Blueprints scripts and operations scripts
to make work with db easier without need of working on  raw SQL's
This tables will be develop in future"""

from .database import db


class User(db.Model):
    """The table hold data about users"""
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    created = db.Column(db.DateTime)
    recipes = db.relationship('Recipes', backref='user')


class Recipes(db.Model):
    """Table holds information about recipes setted up by users, the data is pernament,
    in future it will be develop to distince personal users recipes and shared publicy recipes"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    created = db.Column(db.DateTime)
    status = db.Column(db.String(200))
    timers = db.relationship('Timers', backref='id')


class Timers(db.Model):
    """Table holds currently running timers and bind them with recipes of users and ingredients connected to this timer
    this data is for now efemeric and deleted after user finish operate recipe"""
    due_time = db.Column(db.DateTime, primary_key=True)
    recipe = db.Column(db.Integer, db.ForeignKey(Recipes.id))
    ingredient = db.relationship('Ingredients', backref='timers')


class Ingredients(db.Model):
    """Table holds information about ingredients,
    in future it will be develop to hold information about differents times of cooking based on producer,
     averange data and personal preferences of users"""
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(200))
    timer = db.Column(db.Integer, db.ForeignKey(Timers.due_time))


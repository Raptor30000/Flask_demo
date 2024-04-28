from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    created = db.Column(db.DateTime)
    recipes = db.relationship('Recipes', backref='user')


class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    created = db.Column(db.DateTime)
    status = db.Column(db.String(200))
    timers = db.relationship('Timers', backref='id')


class Timers(db.Model):
    """Table holds currently running timers and bind them with recipes of users and ingredients to use on this timer"""
    due_time = db.Column(db.DateTime, primary_key=True)
    recipe = db.Column(db.Integer, db.ForeignKey(Recipes.id))
    ingredient = db.relationship('Ingredients', backref='timers')


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(200))
    timer = db.Column(db.Integer, db.ForeignKey(Timers.due_time))


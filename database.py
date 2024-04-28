"""Purpouse of this files is to avoid circullar import when models are imported to __init__
 while models need db object to be definied.
 By defining SQLAlchemy nstance here it can be imported both in models and __init__
 so in __init__ models are imported without error"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

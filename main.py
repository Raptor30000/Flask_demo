"""This Bluepring defines endpoints accessible for not authorized users,
 with are not included in the autorization process
 for autorization process use auth Blueprint"""

from flask import Blueprint, jsonify, request
from .models import *
from . import db

#creating a Flask Blueprint instance to be register in __init__ and to attach main endpoint to it
main = Blueprint("main", __name__)


@main.route('/', methods=['GET'])
def test():
    """Endpoint dedicated to integration purpouse to check if you have acces to api"""
    return jsonify("This is test response to check if you have access to this API")


@main.route('/', methods=['POST'])
def test_echo():
    request_body = request.json
    return jsonify(request_body)

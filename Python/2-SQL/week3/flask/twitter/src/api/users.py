from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Tweet, likes_table
import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix = '/users')

@bp.route('', methods=['GET']) # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all() # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize()) # build list of Users as dictionaries
    return jsonify(result) # return JSON response

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())

@bp.route('', methods=['POST'])
def create():
    # req body must contain username and password
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    username_from_request = request.json['username']
    password_from_request = request.json['password']
    # checking the length of username and password
    if len(username_from_request) < 3 or len(password_from_request) < 8:
        return abort(400)
    
    # insert user
    u = User(
        username=username_from_request,
        password=scramble(password_from_request)
    )
    db.session.add(u) # prepare CREATE statement
    db.session.commit() # execute CREATE statement
    return jsonify(u.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u) # prepare DELETE statement
        db.session.commit() # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    
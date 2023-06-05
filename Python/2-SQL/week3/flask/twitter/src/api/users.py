from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Tweet, likes_table
import sqlalchemy
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
    u = User.query.get_or_404(id)
    
    if 'username' in request.json and 'password' in request.json:
        username_from_request = request.json['username']
        password_from_request = request.json['password']
        if len(username_from_request) < 3 or len(password_from_request) < 8:
            return abort(400)
       
        try:
            u.username = username_from_request
            u.password = scramble(password_from_request) 
            db.session.commit() # execute update statement
            return jsonify(u.serialize())
        except:
        # something went wrong :(
            return jsonify(False)
    
    elif 'username' in request.json:
        username_from_request = request.json['username']
        if len(username_from_request) < 3:
            return abort(400)
        
        try:
            u.username = username_from_request
            db.session.commit() # execute update statement
            return jsonify(u.serialize())
        except:
        # something went wrong :(
            return jsonify(False)
    
    elif 'password' in request.json:
        password_from_request = request.json['password'] 
        if len(password_from_request) < 8:
            return abort(400)
        
        try:
            u.password = scramble(password_from_request) 
            db.session.commit() # execute update statement
            return jsonify(u.serialize())
        except:
        # something went wrong :(
            return jsonify(False)
    
    else:
        return abort(400)

@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    u = User.query.get_or_404(id)
    result = []
    for t in u.liked_tweets:
        result.append(t.serialize())
    return jsonify(result)

#Bonus Task 1

@bp.route('/<int:id>/likes', methods=['POST'])
def likes(id: int):
    # req body must contain tweet_id
    
    if 'tweet_id' not in request.json:
        return abort(400)
    
    tweet_id_from_request = request.json['tweet_id']
    id_from_request = id
    u = User.query.get_or_404(id_from_request)
    t = Tweet.query.get_or_404(tweet_id_from_request)
    
    # insert likes
    new_likes = {"user_id": id_from_request, "tweet_id": tweet_id_from_request}
    insert_likes_query = likes_table.insert().values(new_likes)

    try:
        db.session.execute(insert_likes_query) 
        db.session.commit() 
        return jsonify(True)
    except:
    # something went wrong :(
        return jsonify(False)
   
#Bonus Task 2

@bp.route('/<int:userid>/likes/<int:tweetid>', methods=['DELETE'])
def unlike(userid: int, tweetid: int):
   
    tweet_id_from_request = tweetid
    id_from_request = userid
    u = User.query.get_or_404(id_from_request)
    t = Tweet.query.get_or_404(tweet_id_from_request)
    
    # delete likes
    stmt = sqlalchemy.delete(likes_table).where(
    sqlalchemy.and_(
        likes_table.c.user_id == id_from_request,
        likes_table.c.tweet_id == tweet_id_from_request
    )
)

    try:
        db.session.execute(stmt) 
        db.session.commit() 
        return jsonify(True)
    except:
    # something went wrong :(
        return jsonify(False) 
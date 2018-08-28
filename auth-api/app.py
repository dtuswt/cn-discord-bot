from flask import Flask
from flask import request, Response, jsonify
from functools import wraps
from redis import Redis

from user_administration import check_auth
from authentication_error import AuthenticationError

import sys

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route("/")
def hello():
    redis.incr("hits")
    return f"This Compose/Flask demo has been viewed {int(redis.get('hits'))} times."

@app.route("/test")
def test():
    return "Hello, World!!!"

# def auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         authorization = request.authorization
#         # if not authorization or not check_auth(authorization.username, authorization.password):
#         try:
#             authenticate()
#         except AuthenticationError:
#             return Response('Could not verify user credentials.', 401, {'WWW-Authenticate':'Basic realm="Login Required"'})
#         return decorated

@app.route("/login/<discord_id>", methods=['POST', 'DELETE'])
def connect(discord_id):
    if request.method == "DELETE":
        redis.delete(discord_id)
        return jsonify(message=f"User {discord_id} has been deleted"), 204

    redis_user = redis.hgetall(discord_id)

    if redis_user != {}:
        # redis.delete(discord_id)
        username = redis_user[b'username'].decode()
        password = redis_user[b'password'].decode()

        if password == "None":
            set_user(discord_id)
            # return jsonify(message=f"A password has been set for user {discord_id}")
            return jsonify(discord_id=discord_id, username=username, password=password), 204
        return jsonify(discord_id=discord_id, username=username, password=password)
    else:
        return set_user(discord_id)
        # return Response("User created", 201)
    # return f"User was not found, has been set now."
    
def set_user(discord_id):
    username = request.values.get('username')
    password = request.values.get('password')

    if password != None:
        password = check_auth(username, password)

    if password == False:
        return auth_error()

    redis.hmset(discord_id, {'username': username, 'password': password})
    return jsonify(discord_id=discord_id, username=username, password=password), 201

def auth_error():
    # return Response(jsonify({'message': 'Could not verify user credentials.'}), 401, {'WWW-Authenticate':'Basic realm="Login Required"'})
    return jsonify(message='Could not verify user credentials.'), 401

# def check_auth(username, password):
#     try:
#         authenticate(username, password)
#     except AuthenticationError:
#         return False    
#     return True

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

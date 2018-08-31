from flask import Flask
from flask import request, Response, jsonify
from functools import wraps
from redis import Redis
from secrets import token_urlsafe

from user_administration import check_auth, get_redis_user
from authentication_error import AuthenticationError
from dtu_user import DtuUser
from inside import Inside

import sys

app = Flask(__name__)
redis = Redis(host="redis", port=6379)

@app.route("/")
def hello():
    return jsonify(message="This is DTU Compute Discord API", source="https://github.com/dtuswt/cn-discord-bot")

@app.route("/user/<discord_id>")
def get_user(discord_id):
    username, password = get_redis_user(redis, discord_id)
    if username == None:
        return jsonify(message="User not found"), 404
    return jsonify(username=username, password=password, discord_id=discord_id)

@app.route("/user/<discord_id>/info")
def getstuff(discord_id):
    username, password = get_redis_user(redis, discord_id)

    if username == None:
        return jsonify(message=f"User '{discord_id}' could not be found."), 404

    user = DtuUser(username, None, password)
    inside = Inside(user)

    userinfo = inside.get_user_info()

    # return userinfo
    return jsonify(userinfo)

@app.route("/login/<discord_id>", methods=['POST', 'DELETE'])
def connect(discord_id):
    if request.method == "DELETE":
        redis.delete(discord_id)
        return jsonify(message=f"User {discord_id} has been deleted"), 204

    redis_user = redis.hgetall(discord_id)

    if redis_user != {}:
        username = redis_user[b'username'].decode()
        password = redis_user[b'password'].decode()
        token = redis_user[b'token'].decode()

        if password == "None":
            set_user(discord_id)
            return jsonify(discord_id=discord_id, username=username, password=password, token=token), 204
        return jsonify(discord_id=discord_id, username=username, password=password, token=token)
    else:
        return set_user(discord_id)
    
def set_user(discord_id):
    username = request.values.get('username')
    password = request.values.get('password')

    if password != None:
        password = check_auth(username, password)

    if password == False:
        return auth_error()

    token = token_urlsafe(32)
    redis.hmset(discord_id, {'username': username, 'password': password, 'token': token})
    return jsonify(discord_id=discord_id, username=username, password=password, token=token), 201

def auth_error():
    return jsonify(message='Could not verify user credentials.'), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

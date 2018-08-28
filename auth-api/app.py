from flask import Flask
from redis import Redis
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

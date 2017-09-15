from flask import Flask
from redis import Redis, RedisError
import string
import random
import os
import socket


# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():


    html ="Haslo: <b>: {haslo} "
    return html.format(haslo=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(6)))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

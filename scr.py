from flask import Flask
from redis import Redis, RedisError
from random import randint
import os
import socket


# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():


    html ="Liczba: <b>: {liczba} "
    return html.format(liczba=randint(0,9))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

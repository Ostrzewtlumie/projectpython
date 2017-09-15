#importowanie potrzebnych modulow
from flask import Flask
import os
import string
import random
from random import randint
#konfiguracja Flska v2
app = Flask(__name__)
@app.route("/")
#losowanie i wyswietlanie hasla
def hello():
    html ="Haslo: <b>: {haslo} "
    N=randint(6,12)
    haslo=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N))
    return html.format(haslo=haslo)
#konfiguracja Flska v3
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

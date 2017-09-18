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
    html ="Ilosc wylosowanych hasel: {I}<br>"\
    "Hasla: <b> {haslo}</b><br> "\
    "Aby wylosowac ponownie hasla: <FORM>"\
"<INPUT TYPE='button' onClick='history.go(0)' VALUE='Losuj!'>"\
"</FORM>"
    N=randint(6,12)
    I=randint(1,10)
    a=[]
    f= open('table.txt', 'w')
    for x in range(0, I):
        h=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N))
        f.write(' '.join(a))
        a.append(h)
    f.close()
    return html.format(haslo=a,I=I)
#konfiguracja Flska v3
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

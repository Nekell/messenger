from flask import Flask
from time import time
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return '<b>Hello World!<b>'


@app.route('/status')
def status():
    return {
        'status': True,
        'name': 'My Messenger',
        'time': time(),
        'time2': datetime.now().isoformat(),
        'time3': datetime.now().strftime('%d %B %H:%M')
    }


app.run()

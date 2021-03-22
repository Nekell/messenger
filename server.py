from datetime import datetime
from time import time

from flask import Flask, request, abort

app = Flask(__name__)
messages = [
    {
        'name': 'Jack',
        'text': 'Hello everyone, i`m Jack!',
        'time': 1614887855
    },
    {
        'name': 'Mary',
        'text': 'Hello Jack, i`m Mary.',
        'time': 1614887856
    }
]


@app.route('/')
def hello():
    return '<b>Hello World!<b>'


@app.route('/status')
def status():
    # TODO something cool(возвращал количество человек и сообщений на сервере
    return {
        'status': True,
        'name': 'My Messenger',
        'time': time(),
        'time2': datetime.now().isoformat(),
        'time3': datetime.now().strftime('%d %B %H:%M:%S')
    }


@app.route('/send', methods=['POST'])
def send_message():
    data = request.json()
    if not isinstance(data, dict):
        return abort(400)

    name = data.get('name')
    text = data.get('text')

    if not isinstance(name, str) or len(name) == 0:
        return abort(400)

    if not isinstance(text, str) or len(text) == 0 or len(text) > 1000:
        return abort(400)

    message = {
        'name': name,
        'text': text,
        'time': time()
    }
    messages.append(message)

    # if message == '/help':
    #     messages.append({
    #         'name': 'bot',
    #         'text': 'Я сам ничего не знаю',
    #         'time': time()
    #     })
    # TODO перенести бота на ресивер

    return {'ok': True}


@app.route('/messages')
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)

    response = []
    for message in messages:
        if message['time'] > after:
            response.append(message)
    return {'messages': response[:50]}


app.run()

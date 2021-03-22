from datetime import datetime
from time import sleep

from requests import get


def print_message(income_message):
    dt = datetime.fromtimestamp(income_message['time'])
    dt_str = dt.strftime('%d %B %H:%M:%S')
    print(income_message[dt_str, income_message['name']])
    print(income_message['text'])
    print()


after = 0

while True:
    response = get(
        'http://127.0.0.1:5000/messages',
        params={'after': 0})

    messages = response.json()['messages']
    for message in messages:
        print_message(message)
        after = message['time']

    sleep(1)

from PyQt6 import QtCore, QtGui, QtWidgets

from client_ui import Ui_MainWindow
from datetime import datetime

import requests


class Messenger(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.pressed.connecr(self.send_message)
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def print_messages(self, message):
        dt = datetime.fromtimestamp(message['time'])
        dt_str = dt.strftime('%d %B %H:%M:%S')
        self.textBrowser.append(dt_str + ' ' + message['name'])
        self.textBrowser.append(message['text'])
        self.textBrowser.append('')

    def get_messages(self):
        response = requests.get(
            'http://127.0.0.1:5000/messages',
            params={'after': self.after})

        messages = response.json()['messages']
        for message in messages:
            self.print_message(message)
            self.after = message['time']

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        try:
            response = requests.post(
                'http://127.0.0.1:5000/send',
                json={'name': name, 'text': text}
            )
        except:
            self.textBrowser.append('Server down')
            self.textBrowser.append('Try again later')
            self.textBrowser.append('')
            return

        if response.status_code != 200:
            self.textBrowser.append('Nickname and message must not be empty. Message must be less than 1000 characters')
            self.textBrowser.append('')
            return
        self.textEdit.clear()


app = QtWidgets.QApplication([])
window = Messenger()
window.show()
app.exec()

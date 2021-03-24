from PyQt6 import QtCore, QtGui, QtWidgets

from client_ui import Ui_MainWindow

import requests


class Messenger(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.pressed.connecr(self.send_message)




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

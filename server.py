from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<b>Hello World!<b>"


@app.route("/page2")
def page2():
    return "<b>Page 2<b>"


app.run()

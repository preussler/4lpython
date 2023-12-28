from os import getenv

import flask

from dotenv import load_dotenv

load_dotenv()

app = flask.Flask(__name__)

@app.route("/login")
def login():
    return flask.render_template('login.html')


@app.route("/")
def profile():
    return flask.render_template('index.html')

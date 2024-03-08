#!/usr/bin/python3
""" Module starts a Flask web app """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return ('C {}'.format(text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    text = text.replace('_', ' ')
    return ("Python {}".format(text))


@app.route('/number', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def is_num(n):
    int(n)
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

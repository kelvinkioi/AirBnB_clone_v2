#!/usr/bin/python3
"""
script that starts a Flask web application.
"""
from flask import Flask
import re

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Displays "HBNB"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
     display “C ” followed by the value of the text variable
     and replace underscore _ symbols with a space
    """
    new_text = re.sub(r"_", " ", text)
    return f"C {new_text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """
    display “Python ”, followed by the value of the text variable
    and replace underscore _ symbols with a space
    The default value of text is “is cool”
    """
    new_text = re.sub(r"_", " ", text)
    return f"Python {new_text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

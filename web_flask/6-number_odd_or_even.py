#!/usr/bin/python3
"""
script that starts a Flask web application.
"""
from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    display “n is a number” only if n is an integer
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    display a HTML page only if n is an integer
    H1 tag: “Number: n” inside the tag BODY
    """
    return render_template("5-number.html", num=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """
    display a HTML page only if n is an integer
    H1 tag: “Number: n is even|odd” inside the tag BODY
    """
    if n % 2 == 0:
        return render_template(
                "6-number_odd_or_even.html", num=n, result="even")
    else:
        return render_template(
                "6-number_odd_or_even.html", num=n, result="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

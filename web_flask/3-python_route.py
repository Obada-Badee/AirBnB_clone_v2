#!/usr/bin/python3

"""A script to start a flask web application"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """Home route"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbhb():
    """Displays HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """Displays C <text>"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python/")
def python_without_subpath():
    """The python route"""
    return "Python is cool"


@app.route("/python/<text>")
def python_text(text):
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000, debug=True)

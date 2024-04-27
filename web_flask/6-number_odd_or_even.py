#!/usr/bin/python3

"""A script to start a flask web application"""


from flask import Flask, render_template
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


@app.route("/python")
@app.route("/python/<text>")
def python_text(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>")
def is_number(n):
    """The number route"""
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """Display the number template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even_template(n):
    """Display if the number is even or odd"""
    return render_template('6-number_odd_or_even.html', n=n)


if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000, debug=True)

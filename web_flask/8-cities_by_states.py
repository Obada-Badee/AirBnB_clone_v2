#!/usr/bin/python3

"""A script to start the flask web application"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(e):
    """Close the current session"""
    storage.close()


@app.route("/cities_by_states")
def list_states():
    """
    List all the cities by thier states ordered by name from A to Z
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if (__name__ == "__main__"):
    app.run(host="0.0.0.0")

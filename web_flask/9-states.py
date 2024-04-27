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


@app.route("/states")
def list_states():
    """
    List all the states
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>")
def state_with_id(id):
    """
    List a state with the list of City objects linked to the State
    """
    states = storage.all(State)
    state = None
    for s in states.values():
        if s.id == id:
            state = s
            break

    return render_template('9-states.html', state=state)


if (__name__ == "__main__"):
    app.run(host="0.0.0.0")

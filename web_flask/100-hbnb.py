#!/usr/bin/python3

"""A script to start the flask web application"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(e):
    """Close the current session"""
    storage.close()


@app.route("/hbnb")
def hbnb():
    """
    List a state with the list of City objects linked to the State
    """
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)

    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places)


if (__name__ == "__main__"):
    app.run(host="0.0.0.0", debug=True)

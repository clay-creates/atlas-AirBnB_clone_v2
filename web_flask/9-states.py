#!/usr/bin/python3
""" Starts a flask app """
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception=None):
    storage.close()



@app.route('/states', strict_slashes=False)
def states():
    state = storage.all('State').order_by('name')
    return render_template('9-states.html', state=state)


@app.route('/states/<int:state_id>', strict_slashes=False)
def state(state_id):
    state = storage.get('State', state_id)
    if state:
        cities = state.cities.order_by('name')
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return "Not found!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#!/usr/bin/python3
""" Starts a flask web app """
from flask import Flask, render_template
import models


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    return render_template('8-cities_by_states.py', states=models.storage.all("State").values())


@app.teardown_appcontext()
def teardown_db():
    models.storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
import models


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = models.storage.all("State").values()
    states_sort = sorted(states, key=lambda state: state.name)
    states_html = ''.join(['<li>{}: <b>{}</b></li>'.format(state.id, state.name)
                           for state in states_sort])
    return render_template("7-states_list.html")


@app.teardown_appcontext
def teardown_db(exception=None):
    models.storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

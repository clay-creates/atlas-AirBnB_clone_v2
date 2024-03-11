#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
import mysql.connector
import models


# MySQL Setup
database = mysql.connector.connect(
    host = 'localhost',
    user = 'hbnb_dev',
    pwd = 'hbnb_dev_pwd',
    db = 'hbnb_dev_db',
)
cursor = database.cursor()


# Execute SQL File
with open('100-hbnb.sql', 'r') as f:
    sql_commands = f.read()
cursor.execute(sql_commands)
database.commit()


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", states=models.storage.all("State").values())


@app.teardown_appcontext
def teardown_db(exception=None):
    models.storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

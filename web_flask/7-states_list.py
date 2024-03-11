#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
from sqlalchemy import create_engine, text
import os
import models


app = Flask(__name__)


# Set ENV Variables
user = os.getenv('HBNB_MYSQL_USER', 'hbnb_dev')
pwd = os.getenv('HBNB_MYSQL_PWD', 'hbnb_dev_pwd')
host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
db = os.getenv('HBNB_MYSQL_DB', 'hbnb_dev_db')
env = os.getenv('HBNB_ENV')
url = "mysql+mysqldb"

# Set DB connection
connect = "{0}://{1}:{2}@{3}:3306/{4}".format(url, user, pwd, host, db)

# Create engine
engine = create_engine(connect, pool_pre_ping=True, echo=True)

# Execute SQL commands from file
def execute_sql_file(file_path):
    with engine.connect() as con:
        with open(file_path) as file:
            query = text(file.read())
            con.execute(query)

# Execute file before running app
execute_sql_file('100-hbnb.sql')

@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", states=models.storage.all("State").values())


@app.teardown_appcontext
def teardown_db(exception=None):
    models.storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

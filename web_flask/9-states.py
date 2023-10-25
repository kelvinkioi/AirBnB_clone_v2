#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """fetching data from storage engine"""
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """list of City objects linked to the State"""
    state = None
    for i in storage.all('State').values():
        if i.id == id:
            state = i
            break
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def close_DB(exception):
    """  remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

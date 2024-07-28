#!/usr/bin/python3
"""App to generate html lists of all states from storage"""
from flask import Flask, render_template
from models import storage
app = Flask('web_flask')
app.url_map.strict_slashes = False

@app.route('/states_list')
def list_of_states():
    """Rendering html with the unordered list of all states from `storage`"""
    states = sorted(storage.all('State').values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Closing the file storage"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""list of all states from storage"""
from flask import Flask, render_template
from models import storage
app = Flask('web_flask')
app.url_map.strict_slashes = False


@app.route('/states/<id>')
@app.route('/states', defaults={'id': None})
def specific_state(id):
    """alphabetical list of states or specific state entry with `id` a valid identifier"""
    states = storage.all('State')
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)

@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close file storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

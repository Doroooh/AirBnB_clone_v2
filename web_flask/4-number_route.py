#!/usr/bin/python3
"""  Add a view function to display a variable k only if integer """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    """Displays Hello HBNB! """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello():
    """Displays HBNB"""
    return 'HBNB'

@app.route('/c/<text>')
def c_text(text):
    """Substituting the text with a variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Substituting the text with a variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def number_text(k):
    """Display k if variable an integer."""
    return '{} is a number'.format(k)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

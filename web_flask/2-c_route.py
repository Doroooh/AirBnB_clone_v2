#!/usr/bin/python3
""" the Script that starts the Flask web app with a three  view function """

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    """ To return the text """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello():
    """ to return other text """
    return 'HBNB'

@app.route('/c/<text>')
def c_text(text):
    """ to replace text with the variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

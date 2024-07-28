#!/usr/bin/python3
""" A Simple Flask web app"""
from flask import Flask
app = Flask('web_flask')
app.url_map.strict_slashes = False

@app.route('/')
def hello_route1():
    """ To display the phrase 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello_route2():
    """displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def hello_route3(text):
    """Return 'C ' and is then followed by a html request text"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is cool'})
def hello_route4(text):
    """Displays 'Python is cool'"""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

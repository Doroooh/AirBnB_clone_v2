#!/usr/bin/python3
"""web app"""
from flask import Flask, render_template
app = Flask('web_flask')
app.url_map.strict_slashes = False

@app.route('/')
def hello_route1():
    """displays 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello_route2():
    """Displays'HBNB'"""
    return 'HBNB'
@app.route('/c/<text>')
def hello_route3(text):
    """Return 'C ' and the html text"""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is cool'})
def hello_route4(text):
    """Display 'Python is cool'"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:k>')
def hello_route5(k):
    """Display formatted number if can be converted to an int"""
    return '{:d} is a number'.format(k)

@app.route('/number_template/<int:k>')
def hello_route6(k):
    """Display the html template containing the number `k`"""
    return render_template('5-number.html', k=k)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" web app"""
from flask import Flask, render_template
app = Flask('web_flask')
app.url_map.strict_slashes = False

@app.route('/')
def hello_route1():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello_route2():
    """Display 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>')
def hello_route3(text):
    """Return 'C ' and html text """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>')
@app.route('/python/', defaults={'text': 'is cool'})
def hello_route4(text):
    """Return 'Python is cool'"""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:k>')
def hello_route5(k):
    """format as a number if can convert to an int"""
    return '{:d} is a number'.format(k)

@app.route('/number_template/<int:n>')
def hello_route6(k):
    """Return html template with the number `k`"""
    return render_template('5-number.html', k=k)

@app.route('/number_odd_or_even/<int:k>')
def hello_route7(k):
    """Return rendered html containing logic that determines whether
    `k` is even or odd and displays the result in an <h1> tag"""
    return render_template('6-number_odd_or_even.html', k=k)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

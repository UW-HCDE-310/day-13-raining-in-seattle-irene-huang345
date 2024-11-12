import urllib.request, urllib.parse, urllib.error, json, flask
import requests

from flask import Flask

app = Flask(__name__)

@app.route("/")

def is_it_raining_in_seattle():
    with urllib.request.urlopen('http://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        return "<p>True</p>"
    else:
        return "<p>False</p>"

if __name__ == "__main__":
    app.run(debug=True)


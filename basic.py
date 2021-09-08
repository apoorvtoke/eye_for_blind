#!/usr/bin/env python
# coding: utf-8

from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home directory
def hello():
    return "Welcome to the Eye For Blind Prediction"

# If you want to run this app, you must call the run()
if __name__=='__main__':
    app.run(debug=True)
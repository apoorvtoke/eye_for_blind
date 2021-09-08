#!/usr/bin/env python
# coding: utf-8

# import Flask class from the flask module
# from sklearn.externals import joblib
from flask import Flask, request, render_template
import numpy as np
from keras.models import load_model
import h5py

# Create Flask object to run
app = Flask(__name__)

# Load the model from the file
# iris_model = load_model('eye_for_blind.hdf5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get values from browser
    int_features = [ int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = client_model.predict(final_features)
    # output = round(prediction[0], 2)
    output = prediction
    return (output)


if __name__ == "__main__":
    # Start Application
    app.run()

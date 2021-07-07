# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 00:15:06 2021

@author: snara016
"""

from flask import Flask, request
import pandas as pd
import pickle
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)
# open classifier.pkl file in read byte mode 
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict_bank_note_auth():
#    variance = request.args.get('variance')
#    skewness = request.args.get('skewness')
#    curtosis = request.args.get('curtosis')
#    entropy = request.args.get('entropy')
#    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
#    return "The predicted value is " + str(prediction)
    
    """Let's Authenticate the Bank Note
    
    This is using docstrings for specifications.
    ---
    parameters:
        -   name: variance 
            in: query
            type: number
            required: true
        -   name: skewness 
            in: query
            type: number
            required: true
        -   name: curtosis 
            in: query
            type: number
            required: true
        -   name: entropy 
            in: query
            type: number
            required: true
    responses:
        200:
            description: The output values
    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is " + str(prediction)


@app.route('/predict_file',methods=['POST'])
def predict_bank_note_auth_file():

    
    """Let's Authenticate the Bank Note
    
    This is using docstrings for specifications.
    ---
    parameters:
        -   name: file 
            in: formData
            type: file
            required: true
    responses:
        200:
            description: The output values
    """    

    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "The predicted values for the csv is " + str(list(prediction))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
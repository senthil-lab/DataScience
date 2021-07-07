# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 00:15:06 2021

@author: snara016
"""

#from flask import Flask, request
import pandas as pd
import pickle
#import flasgger
#from flasgger import Swagger
import streamlit as st

from PIL import Image

#app=Flask(__name__)
#Swagger(app)
# open classifier.pkl file in read byte mode 
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict')
def predict_bank_note_auth(variance,skewness,curtosis,entropy):
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
#    variance = request.args.get('variance')
#    skewness = request.args.get('skewness')
#    curtosis = request.args.get('curtosis')
#    entropy = request.args.get('entropy')
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted value is " + str(prediction)


#@app.route('/predict_file',methods=['POST'])
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

#    df_test = pd.read_csv(request.files.get("file"))
#    prediction = classifier.predict(df_test)
#    return "The predicted values for the csv is " + str(list(prediction))
    pass

def main():
    st.title("Bank Authentication")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align=center">StreamLit Bank Authentication ML App</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input('variance','Type Here')
    skewness = st.text_input('skewness','Type Here')
    curtosis = st.text_input('curtosis','Type Here')
    entropy = st.text_input('entropy','Type Here')
    result = ''
    if st.button('Predict'):
        result = predict_bank_note_auth(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button('About'):
        st.text('Built with Streamlit')

if __name__ == '__main__':
    main()
    
    
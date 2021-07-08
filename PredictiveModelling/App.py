# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 15:51:15 2021

@author: snara016

Predictive Modelling: Car Prediction
"""

from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = float(request.form['Kms_Driven'])
        Owner = int(request.form['Owner'])
        Fuel_Type = request.form['Fuel_Type']
        if (Fuel_Type=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        elif (Fuel_Type=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
        Year=2020-Year
        Seller_Type=request.form['Seller_Type']
        if(Seller_Type=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission=request.form['Transmission']
        if(Transmission=='Manual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
        print('Present_Price: ', Present_Price)
        print('Kms_Driven: ', Kms_Driven)
        print('Owner: ',Owner)
        print('Year: ',Year)
        print('Fuel_Type_Diesel: ', Fuel_Type_Diesel)
        print('Fuel_Type_Petrol:', Fuel_Type_Petrol)
        print('Seller_Type_Individual: ', Seller_Type_Individual)
        print('Transmission_Manual:',Transmission_Manual)
        prediction=model.predict([[Present_Price,Kms_Driven,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)        
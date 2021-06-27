#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:43:56 2021

@author: keerthananatarajan
"""
# Importing essential libraries

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:43:56 2021

@author: keerthananatarajan
"""
# Importing essential libraries

#from flask import flask
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'Diabetess.pkl'
classifier = pickle.load(open('Diabetess.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
	return render_template('./index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        preg = request.form['pregnancies']
        glucose = request.form['glucose']
        bp = request.form['bloodpressure']
        st = request.form['skinthickness']
        insulin = request.form['insulin']
        bmi = request.form['bmi']
        dpf = request.form['dpf']
        age = request.form['age']

        
        
        data = np.array([[0,0,0,0,0,0,0,0,0,0,0,preg, glucose, bp, st, insulin, bmi, dpf, age,0,0,0,0,0]])
       
        my_prediction = classifier.predict(data)
        print(my_prediction)
        return render_template('result.html', prediction=my_prediction)
        

if __name__ == '__main__':
	app.run(debug=True)


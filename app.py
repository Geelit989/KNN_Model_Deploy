# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o0f8icfCkhaSYjtO6z-crB-2taXKZbAr
"""

from flask import Flask, render_template, request
import numpy as np
import pickle
import joblib
app = Flask(__name__)
filename = 'knn_cancer 2.pkl'
#model = pickle.load(open(filename, 'rb'))
model = joblib.load(filename)
#model = joblib.load(filename)
@app.route('/')
def index(): 
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    Mean_Concave_Points = request.form['0']
    Worst_Perimeter = request.form['1']
    Worst_Concave_Points = request.form['2']

    
      
    pred = model.predict(np.array([['0', '1', '2']]))
    print(pred)
    return render_template('index.html', predict=str(pred))


if __name__ == '__main__':
    app.run

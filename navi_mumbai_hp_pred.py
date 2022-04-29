from flask import Flask, render_template, request
from flask import render_template
import pickle
import pandas as pd
import numpy as np


app=Flask(__name__)

df = pd.read_csv('E:/Python programs/Project/project.csv')
pipe = pickle.load(open('hp_prediction.pkl', 'rb'))

@app.route('/')#Route Home page
def hello_world():

    locations = df['location'].unique()
    return render_template("hp_pred.html", locations= locations)

@app.route('/predict', methods=['POST'])#Route Home page
def predict():

    location = request.form.get('location')
    bhk = request.form.get('bhk')
    bathroom = request.form.get('bathroom')
    total_area = request.form.get('total_sqft')

    input = pd.DataFrame([[location, bhk, bathroom, total_area]], columns=['location', 'bedroom', 'bathroom', 'Total Area'])

    prediction = pipe.predict(input)[0]



    return str(np.round(prediction, 2))


# To which url we want to go redirect will direct it to that url
if __name__=='__main__':
    app.run(debug=True)    
from flask import Flask, render_template
import random as rd
from datetime import datetime as dt
import requests as rq

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello world!</h1>'


@app.route('/<name>')
def name_info(name):
    dt_now = dt.now()
    dt_year = dt_now.year

    # Call the API functions with the provided name
    gender = guess_gender(name)
    age = guess_age(name)


    return render_template('index.html', name=name, year=dt_year, gender=gender, age=age)

def guess_age(name):
    response = rq.get(f'https://api.agify.io?name={name}')
    response.raise_for_status()
    age = response.json()["age"]
    return age

def guess_gender(name,country='US'):
    response = rq.get(f'https://api.genderize.io?name={name}&country_id={country}')
    response.raise_for_status()
    gender = response.json()["gender"]
    return gender

if __name__ == "__main__":
    app.run(debug=True) 
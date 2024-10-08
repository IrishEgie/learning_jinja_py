from flask import Flask, render_template
import random as rd
from datetime import datetime as dt


app = Flask(__name__)

@app.route('/')
def home():
    rand_num = rd.randint(1,10)
    dt_year = dt.year
    return render_template('index.html', num=rand_num, year=dt_year)

if __name__ == "__main__":
    app.run(debug=True)
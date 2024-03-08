# flask --app data_server run
from flask import Flask
from flask import render_template
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f= open("data/life_expectancy.json", "r")
    data=json.load(f)
    f.close()
    years = sorted(data["Canada"].keys())
    Canada_list = []
    for n in years:
        Canada_list.append(data["Canada"][n])
    print(Canada_list)

    
    
      
    
    return render_template('index.html',years = sorted(data["Canada"].keys()))

@app.route('/year')
def year():
    return render_template('year.html')


app.run(debug=True)

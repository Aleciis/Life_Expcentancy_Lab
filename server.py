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
    canada_years = sorted(data["Canada"].keys())
    Canada_list = []
    canada_data = data["Canada"]
    for n in range(len(canada_years)-1):
        start_x = canada_years[n] #generate endpoints for each line segment
        stop_x = canada_years[n+1]
        Canada_list.append([data["Canada"][start_x],data["Canada"][stop_x]] )
    
    US_data= data["United States"]
    US_years = sorted(data["United States"].keys())
    US_list = []
    for n in range(len(US_years)-1):
        start_x = US_years[n] #generate endpoints for each line segment
        stop_x = US_years[n+1]
        US_list.append([data["United States"][start_x],data["United States"][stop_x]] )

    mexico_data=data["Mexico"]
    mexico_years = sorted(data["Mexico"].keys())
    Mexico_list = []
    for n in range(len(mexico_years)-1):
        start_x = mexico_years[n] #generate endpoints for each line segment
        stop_x = mexico_years[n+1]
        Mexico_list.append([data["Mexico"][start_x],data["Mexico"][stop_x]] )
   

    Avg_list = []
    for (a,b,c) in zip(canada_data, US_data, mexico_data):
        avg_sum=0
        avg_sum= (canada_data[a]+US_data[b]+mexico_data[c])/3
        Avg_list.append(avg_sum)
    
    Avg_coords = []
    for n in range(len(Avg_list)-1):
        start_x = Avg_list[n]
        stop_x = Avg_list[n+1]
        Avg_coords.append([start_x, stop_x])
   
    print(sorted(data["Canada"].keys()))
    
      
    
    return render_template('index.html',years = sorted(data["Canada"].keys()), canada_data= Canada_list, US_data = US_list, mexico_data=Mexico_list, avg_data=Avg_coords)

@app.route('/year')
def year():
    f= open("data/life_expectancy.json", "r")
    data=json.load(f)
    f.close()
    return render_template('year.html',years = sorted(data["Canada"].keys()) )


app.run(debug=True)

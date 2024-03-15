# flask --app data_server run
from flask import Flask
from flask import render_template
import json
from flask import request
import math


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
    
    all_nums=[]
    for (a,b,c) in zip(canada_data, US_data, mexico_data):
        avg_sum=0
        avg_sum= (canada_data[a]+US_data[b]+mexico_data[c])/3
        
        Avg_list.append(avg_sum)
        all_nums.append(canada_data[a])
        all_nums.append(US_data[b])
        all_nums.append(mexico_data[c])

    

    
    
    all_sorted = sorted(all_nums)
    lowest = all_sorted[0]
    highest = all_sorted[-1]
    print(lowest,highest)
    #print(all_sorted)
    avg=0
    universal_avg=[]
    for n in all_sorted:
        avg=avg+n
        total=avg/len(all_sorted)
    universal_avg.append(total)
    universal_avg.append(total)
    print(universal_avg)
    
    all_weighted =[]
    for nums in all_nums:
        all_weighted.append( (nums- lowest) / (highest - lowest) * (100 - 0) - 0)
    

    mexico_weighted=[]
    for nums in mexico_data:
         mexico_weighted.append( (mexico_data[nums]- lowest) / (highest - lowest) * (100 - 0) - 0)
    #print(mexico_weighted)

    US_weighted=[]
    for nums in US_data:
         US_weighted.append( (US_data[nums]- lowest) / (highest - lowest) * (100 - 0) - 0)
    #print(US_weighted)

    canada_weighted=[]
    for nums in canada_data:
         canada_weighted.append( (canada_data[nums]- lowest) / (highest - lowest) * (100 - 0) - 0)
    #print(canada_weighted)
         
    

    canada_weighted_points = []
    for n in range(len(canada_weighted)-1):
        start_x = n #generate endpoints for each line segment
        stop_x = n+1
        
        canada_weighted_points.append( [canada_weighted[start_x],canada_weighted[stop_x]] )
    

    US_weighted_points = []
    for n in range(len(US_weighted)-1):
        start_x = n #generate endpoints for each line segment
        stop_x = n+1
        
        US_weighted_points.append( [US_weighted[start_x],US_weighted[stop_x]] )


    mexico_weighted_points = []
    for n in range(len(mexico_weighted)-1):
        start_x = n #generate endpoints for each line segment
        stop_x = n+1
        
        mexico_weighted_points.append( [mexico_weighted[start_x],mexico_weighted[stop_x]] )
    

    avg_weighted_points = []
    for n in range(len(Avg_list)-1):
        start_x = n #generate endpoints for each line segment
        stop_x = n+1
        avg_weighted=[]
        for nums in Avg_list:
            avg_weighted.append( (nums- lowest) / (highest - lowest) * (100 - 0) - 0)

        avg_weighted_points.append( [avg_weighted[start_x],avg_weighted[stop_x]] )

    

    Avg_coords = []
    for n in range(len(Avg_list)-1):
        start_x = Avg_list[n]
        stop_x = Avg_list[n+1]
        Avg_coords.append([start_x, stop_x])
   
    data_percentages = ["40","50","60","70","80","90"]
    #print(Avg_coords)
    #print(avg_weighted_points)
    #print(Avg_list)
    
    return render_template('index.html',years = sorted(data["Canada"].keys()), canada_data= canada_weighted_points, US_data = US_weighted_points, mexico_data= mexico_weighted_points, avg_data=avg_weighted_points, percentages=data_percentages)

@app.route('/year')
def year():
    f= open("data/life_expectancy.json", "r")
    data=json.load(f)
    f.close()
    print(f"request.url={request.url}")
    print(f"request.url={request.query_string}")
    title_year = request.args.get('year')
    number_year = int(title_year)
    canada_data = data["Canada"]
    US_data= data["United States"]
    mexico_data=data["Mexico"]
    all_nums=[]
    print(canada_data["2019"])

    

    for (a,b,c) in zip(canada_data, US_data, mexico_data):

        all_nums.append(canada_data[a])
        all_nums.append(US_data[b])
        all_nums.append(mexico_data[c])
    
    all_sorted = sorted(all_nums)
    lowest = all_sorted[0]-20
    highest = all_sorted[-1]
    #print(lowest)
    
    all_weighted =[]
    for nums in all_nums:
        all_weighted.append( (nums- lowest) / (highest - lowest) * (100 - 0) - 0)
    
    #print(all_weighted)
    country_year_data=[]

    for i in range(0,len(all_weighted),3):
        country_year_data.append(all_weighted[i:i+3])
    #print(country_year_data)
    #print(country_year_data[0][0])
    #print(number_year)
    print(country_year_data[(number_year-1960)][0]/100)

  

    color_list=list(range(0,101))

    return render_template('year.html',years = sorted(data["Canada"].keys()), title_year = title_year, Canada_saturation=country_year_data[(number_year-1960)][0], US_saturation=country_year_data[(number_year-1960)][1], Mexico_saturation=country_year_data[(number_year-1960)][2], color_list=color_list, Canada_percent=math.floor(canada_data[title_year]),US_percent=math.floor(US_data[title_year]),Mexico_percent=math.floor(mexico_data[title_year]), universal_avg=72.3 )
# look at demo code request.get to pull a variable out of a url

app.run(debug=True)

from flask import Flask, render_template , json , request
from textblob import TextBlob
from dotenv import load_dotenv
import os
import requests
import messagebox
load_dotenv()
app = Flask(__name__)
global api_key
api_key=os.environ.get("api_key")
print(api_key)
@app.route('/getWeather/',methods=["POST","GET"])
def getWeather():
    cityy=request.form["city"]
    print(cityy)
    details={
        "q":  cityy,
        "aqi":"yes",
        "key":api_key
    }    
    global response
    response = requests.post(url="http://api.weatherapi.com/v1/current.json",data=details)
    
    if(response.status_code==200):
        location=response.json()['location']['name']
        state=response.json()['location']['region']
        country=response.json()['location']['country']
        temperature = response.json()['current']['temp_c'] 
        condition = response.json()['current']['condition']['text']
        icon=response.json()['current']['condition']['icon']
        return render_template("index.html",w_name=location,w_state=state,w_country=country,w_temp = temperature,symbol="° C",w_condition = condition,w_image=icon,isExist=0)

    else:
        return render_template("index.html",w_name="",w_state="",w_country="",w_temp="",w_condition="",w_image="",isExist=1)
@app.route('/')  
def form():
    return render_template("index.html")  

if __name__ == "__main__":
   app.run(debug=True)

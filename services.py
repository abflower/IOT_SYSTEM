# This file contains the functions for the different services
# these function are called by the manage, which also passes 
# the needed arguments.


import json
import logging
import requests


def get_weather(api_key, api_url, city, check):
    api_key = api_key
    api_url = api_url + api_key
    query_url = api_url.format(city)
   

    weather={
        "name": "",
        "temperature": "0",
        "symbol": "",
        "description": "Some error occurred",
        "min": "0",
        "max": "0",
        "hum": "0",
        "pressure": "0"}

    weather['name'] = city

    req = requests.get(query_url)
    

    if '404' in str(req):
        
        weather['description'] = "No weather available"
        
        logging.warn('No weather available for {}.'.format(city))

    if '401' in str(req):
        
        weather['description'] = "Error during request"
        
        logging.warn('An error occurred when requesting weather data for {}'.format(city))
    
    if '200' in str(req):
        data = req.content
        parsed = json.loads(data)
        weather = None
        if parsed.get("weather"):
            url = "http://openweathermap.org/img/w/"
            icon_url = url + parsed["weather"][0]["icon"]+".png"
            weather = {
                "name": parsed["name"],
                "temperature": str(parsed["main"]["temp"]),
                "symbol": icon_url,
                "description": parsed["weather"][0]["description"],
                "min": str(parsed["main"]["temp_min"]),
                "max": str(parsed["main"]["temp_max"]),
                "hum": str(parsed["main"]["humidity"]),
                "pressure": str(parsed["main"]["pressure"])}
    return weather

def test_function(check):
    return 'La la la, test is working :)'

def switch_stove(check):
    if check == 1:
        return 'Stove switched ON'
    elif check == 2:
        return 'Stove switched OFF'
